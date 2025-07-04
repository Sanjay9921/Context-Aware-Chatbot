import React, { useState, useEffect } from 'react';
import {
  Container,
  Typography,
  Box,
  Button,
  TextField,
  Alert,
  Divider,
  Input,
  Stack,
  Paper,
  CircularProgress,
} from '@mui/material';
import UploadFileIcon from '@mui/icons-material/UploadFile';
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';

function App() {
  const [healthStatus, setHealthStatus] = useState('Checking...');
  const [file, setFile] = useState(null);
  const [uploadMessage, setUploadMessage] = useState('');
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);
  const [modelInUse, setModelInUse] = useState('Fetching...');

  useEffect(() => {
  fetch('/api/model')
    .then(res => res.json())
    .then(data => setModelInUse(data.model))
    .catch(() => setModelInUse('Unavailable'));
  }, []);

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setHealthStatus(data.status))
      .catch(() => setHealthStatus('Error connecting to backend'));
  }, []);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setUploadMessage('');
  };

  const handleUpload = async () => {
    if (!file) return setUploadMessage('Please select a PDF file first');
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });
      const data = await res.json();
      if (res.ok) {
        setUploadMessage(`Upload successful! ${data.message}`);
      } else {
        setUploadMessage(`Upload failed: ${data.error}`);
      }
    } catch (err) {
      setUploadMessage('Upload failed: Network error');
    }
  };

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer('');
    try {
      const res = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      if (res.ok) {
        setAnswer(data.answer);
      } else {
        setAnswer(`Error: ${data.error}`);
      }
    } catch {
      setAnswer('Error connecting to backend');
    }
    setLoading(false);
  };

  return (
    <Container maxWidth="md" sx={{ py: 5 }}>
      <Typography variant="h4" gutterBottom>
        Flask Backend Health Check
      </Typography>
      
      <Typography sx={{ mb: 3 }}>
        Status:{' '}
        <Box
          component="span"
          sx={{ color: healthStatus === 'OK' ? 'green' : 'red', fontWeight: 'bold' }}
        >
          {healthStatus}
        </Box>
      </Typography>

      <Divider sx={{ my: 4 }} />

      <Typography variant="h5" gutterBottom>
        Upload PDF
      </Typography>

      <Stack direction="row" spacing={2} alignItems="center" sx={{ mb: 2 }}>
        <Input type="file" onChange={handleFileChange} inputProps={{ accept: 'application/pdf' }} />
        <Button
          variant="contained"
          startIcon={<UploadFileIcon />}
          onClick={handleUpload}
          disabled={!file}
        >
          Upload
        </Button>
      </Stack>
      {uploadMessage && (
        <Alert severity={uploadMessage.includes('successful') ? 'success' : 'error'}>
          {uploadMessage}
        </Alert>
      )}

      <Divider sx={{ my: 4 }} />

      <Typography variant="h5" gutterBottom>
        Ask a Question
      </Typography>

      <Box sx={{ mb: 2 }}>
        <TextField
          label="Model in use"
          variant="outlined"
          value={modelInUse}
          InputProps={{ readOnly: true }}
          sx={{ width: '600px' }}
        />
      </Box>

      <Stack direction="row" spacing={2} alignItems="center">
        <TextField
          label="Your question"
          variant="outlined"
          fullWidth
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <Button
          variant="contained"
          onClick={handleAsk}
          startIcon={<HelpOutlineIcon />}
          disabled={loading}
        >
          Ask
        </Button>
      </Stack>

      {loading && (
        <Stack direction="row" spacing={1} alignItems="center" sx={{ mt: 2 }}>
          <CircularProgress size={20} />
          <Typography variant="body2">Please wait, getting the answer...</Typography>
        </Stack>
      )}

      {answer && (
        <Paper elevation={3} sx={{ mt: 3, p: 2 }}>
          <Typography variant="subtitle1" fontWeight="bold">
            Answer:
          </Typography>
          <Typography>{answer}</Typography>
        </Paper>
      )}
    </Container>
  );
}

export default App;
