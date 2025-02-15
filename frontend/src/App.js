import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import ConversionPage from './pages/ConversionPage';

function Home() {
  return (
    <div style={{ textAlign: 'center' }}>
      <h1>Bem-vindo ao ConvertaTXT</h1>
      <p>Utilize a navegação para converter arquivos.</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div>
        <nav style={{ marginBottom: '20px' }}>
          <Link to="/">Home</Link> | <Link to="/conversion">Conversão</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/conversion" element={<ConversionPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
