import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from './AuthContext';
export function ProtectedRoute({ children }) {
  const token = localStorage.getItem('access_token');
  const { user, loading } = useContext(AuthContext);
  if (loading) {
    return <div>Carregando...</div>;
  }

  if (!user || !token) {
    return <Navigate to="/login" />;
  }

  return children;
}