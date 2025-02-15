import React, { useState } from 'react';
import axios from 'axios';

const ConversionPage = () => {
  const [folderPath, setFolderPath] = useState('');
  const [message, setMessage] = useState('');

  const handleConvert = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/convert/', { folder_path: folderPath });
      setMessage(`Tarefa iniciada. Task ID: ${response.data.task_id}`);
    } catch (error) {
      console.error(error);
      setMessage('Erro ao iniciar a conversão.');
    }
  };

  return (
    <div style={{ textAlign: 'center' }}>
      <h1>Seleção de Pasta</h1>
      <p>Informe o caminho completo da pasta que contém os arquivos para conversão:</p>
      <input
        type="text"
        placeholder="Ex.: C:\caminho\para\a\pasta"
        value={folderPath}
        onChange={(e) => setFolderPath(e.target.value)}
        style={{ width: '80%', padding: '8px', fontSize: '16px' }}
      />
      <br />
      <button onClick={handleConvert} style={{ marginTop: '20px', padding: '10px 20px', fontSize: '16px' }}>
        Iniciar Conversão
      </button>
      {message && <p style={{ marginTop: '20px' }}>{message}</p>}
    </div>
  );
};

export default ConversionPage;
