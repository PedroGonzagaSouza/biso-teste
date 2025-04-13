import React, { useState } from 'react';
import UsuariosService from '@/services/UsuariosService';

export function CadastroPage() {
  const [formData, setFormData] = useState({
    nome: '',
    login: '',
    senha: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };
  const [message, setMessage] = useState('');
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Form Data:', formData);
    try {
      const respose = await UsuariosService.postNovoUsuario({
        NOME: formData.nome,
        LOGIN: formData.login,
        SENHA: formData.senha,
      })
      setMessage("Usuário cadastrado com sucesso!");
      console.log("Usuário cadastrado com sucesso!", respose);
    } catch (error) {
      setMessage('Erro ao cadastrar usuário: ' + error.message);
      console.error('Erro ao cadastrar usuário:', error);
    }
    // Aqui você pode adicionar a lógica para enviar os dados para a API
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-6 text-center">Cadastro de Perfil</h1>
        {message && <p className="text-center text-red-500 mb-4">{message}</p>}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="nome" className="block text-gray-700 font-medium mb-2">
              Nome
            </label>
            <input
              type="text"
              id="nome"
              name="nome"
              value={formData.nome}
              onChange={handleChange}
              className="w-full px-4 py-2 border text-black  rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Digite seu nome de usuário"
              required
            />
          </div>

          <div className="mb-4">
            <label htmlFor="login" className="block text-gray-700 font-medium mb-2">
              Login
            </label>
            <input
              type="login"
              id="login"
              name="login"
              value={formData.login}
              onChange={handleChange}
              className="w-full px-4 py-2 border text-black rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Digite seu login"
              required
            />
          </div>

          <div className="mb-6">
            <label htmlFor="senha" className="block text-gray-700 font-medium mb-2">
              Senha
            </label>
            <input
              type="senha"
              id="senha"
              name="senha"
              value={formData.senha}
              onChange={handleChange}
              className="w-full text-black  px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Digite sua senha"
              required
            />
          </div>

          {/* Botão de Cadastro */}
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-200"
          >
            Cadastrar
          </button>
        </form>
      </div>
    </div>
  );
}