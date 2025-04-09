import numpy as np 
import pandas as pd
import sklearn.metrics.pairwise as pw

class TratamentoController:
    
    async def tratamento(filmes: list, ratings: list, filme: str) -> list:
        dadosFilmes = filmes
        dadosRatings = ratings
        
        try:
            ratingsDf = pd.DataFrame(dadosRatings, columns=['userId', 'movieId', 'rating'])
            filmesDf = pd.DataFrame(dadosFilmes, columns=['movieId', 'title', 'genres', 'year'])
            
            df = filmesDf.merge(ratingsDf, on='movieId')
            
            tabelaFilmes = df.pivot_table(index='title', columns='userId', values='rating').fillna(0)
            
            recomendacoes = pw.cosine_similarity(tabelaFilmes)
            recomendacoes = pd.DataFrame(recomendacoes, columns=tabelaFilmes.index, index=tabelaFilmes.index)
           
            return recomendacoes[filme].sort_values(ascending=False).head(10).to_dict()
        except Exception as e:
            print("Erro ao criar DataFrame" , e)
            raise e
    async def tratamento_usuario(filmes: list, ratings: list, usuario_id: int) -> list:
        """
        Gera recomendações personalizadas para o usuário com base no histórico de avaliações.
        """
        try:
            ratings_df = pd.DataFrame(ratings, columns=['userId', 'movieId', 'rating'])
            filmes_df = pd.DataFrame(filmes, columns=['movieId', 'title', 'genres', 'year'])

            # Filtrar avaliações do usuário
            user_ratings = ratings_df[ratings_df['userId'] == usuario_id]
            if user_ratings.empty:
                return {"message": "Nenhum histórico de avaliações encontrado para o usuário."}

            # Calcular similaridade com base nos filmes avaliados
            df = filmes_df.merge(ratings_df, on='movieId')
            tabela_filmes = df.pivot_table(index='title', columns='userId', values='rating').fillna(0)
            similaridade = pw.cosine_similarity(tabela_filmes)
            similaridade_df = pd.DataFrame(similaridade, index=tabela_filmes.index, columns=tabela_filmes.index)

            # Obter recomendações com base nos filmes avaliados pelo usuário
            filmes_assistidos = user_ratings.merge(filmes_df, on='movieId')['title']
            recomendacoes = similaridade_df[filmes_assistidos].mean(axis=1).sort_values(ascending=False)
            recomendacoes = recomendacoes[~recomendacoes.index.isin(filmes_assistidos)].head(10)

            return recomendacoes.to_dict()
        except Exception as e:
            raise Exception(f"Erro ao gerar recomendações: {e}")