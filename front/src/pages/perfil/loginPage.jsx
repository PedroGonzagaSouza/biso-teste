import React, { useState, useContext, useEffect } from 'react';
import { AuthContext } from '@/AuthContext';
import { NavbarLink } from '@/components/header/navbar/navbar-link';
export function LoginPage() {
  const { user, login, logout } = useContext(AuthContext);

  const [formData, setFormData] = useState({ login: '', senha: '' });
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login({ LOGIN: formData.login, SENHA: formData.senha });
      setMessage(`Login realizado com sucesso!`);
      
      
      
    } catch (error) {
      setMessage('Erro ao fazer login.');
      console.error('Erro:', error);
    }
  };
  
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-6 text-center">Login</h1>
        {message && <p className="text-center text-red-500 mb-4">{message}</p>}
        {!user && (
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="login" className="block text-gray-700 font-medium mb-2">
                Login
              </label>
              <input
                type="text"
                id="login"
                name="login"
                value={formData.login}
                onChange={handleChange}
                className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Digite seu login"
                required
              />
            </div>
            <div className="mb-6">
              <label htmlFor="senha" className="block text-gray-700 font-medium mb-2">
                Senha
              </label>
              <input
                type="password"
                id="senha"
                name="senha"
                value={formData.senha}
                onChange={handleChange}
                className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Digite sua senha"
                required
              />
            </div>
            <button
              type="submit"
              className="w-full bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-200"
            >
              Entrar
            </button>
          </form>

        )}
        {user && (
          <div className="text-center">
            <p className="text-gray-700 mb-4">Você já está logado como {user.nome}.</p>
            <button
              onClick={() => {
                logout();
                setMessage('Logout realizado com sucesso!');
              }}
              className="w-full bg-red-500 text-white py-2 px-4 rounded-lg hover:bg-red-600 transition duration-200"
            >
              Logout
            </button>
          </div>
        )}

        <div className='flex flex-row justify-center items-center gap-2 pt-5'>
          {!user && <NavbarLink name={"Novo por aqui? Clique aqui para se cadastrar."} to="/cadastro" className=" text-slate-400 hover:text-black"/>}

        </div>
      </div>
    </div>
  );
}