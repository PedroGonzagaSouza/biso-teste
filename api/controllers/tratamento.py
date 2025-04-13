import numpy as np 
import pandas as pd
import sklearn.metrics.pairwise as pw
from sklearn.feature_extraction.text import TfidfVectorizer
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
        try:
            ratings_df = pd.DataFrame(ratings, columns=['userId', 'movieId', 'rating'])
            filmes_df = pd.DataFrame(filmes, columns=['movieId', 'title', 'genres', 'year'])

            # Filtrar avaliações do usuário
            user_ratings = ratings_df[ratings_df['userId'] == usuario_id]
            if user_ratings.empty:
                return []

            # Calcular similaridade com base nos filmes avaliados
            df = filmes_df.merge(ratings_df, on='movieId')
            tabela_filmes = df.pivot_table(index='title', columns='userId', values='rating').fillna(0)
            similaridade = pw.cosine_similarity(tabela_filmes)
            similaridade_df = pd.DataFrame(similaridade, index=tabela_filmes.index, columns=tabela_filmes.index)

            # Obter recomendações com base nos filmes avaliados pelo usuário
            filmes_assistidos = user_ratings.merge(filmes_df, on='movieId')['title']
            recomendacoes = similaridade_df[filmes_assistidos].mean(axis=1).sort_values(ascending=False)
            recomendacoes = recomendacoes[~recomendacoes.index.isin(filmes_assistidos)].head(10)

            # Adicionar o movieId ao DataFrame de recomendações
            recomendacoes_df = recomendacoes.reset_index()
            recomendacoes_df.columns = ['title', 'similarity_score']
            recomendacoes_df = recomendacoes_df.merge(filmes_df[['title', 'movieId', 'genres', 'year']], on='title', how='left')

            return recomendacoes_df.to_dict(orient='records')
        except Exception as e:
            raise Exception(f"Erro ao gerar recomendações: {e}")
  
    async def filtragem_por_conteudo(filmes: list, ratings: list, usuario_id: int) -> list:
        try:
            filmes_df = pd.DataFrame(filmes, columns=['movieId', 'title', 'genres', 'year'])
            ratings_df = pd.DataFrame(ratings, columns=['userId', 'movieId', 'rating'])

            # Filtrar os filmes avaliados pelo usuário
            user_ratings = ratings_df[ratings_df['userId'] == usuario_id]
            if user_ratings.empty:
                return []

            # Criar uma representação vetorial dos gêneros usando TF-IDF
            tfidf = TfidfVectorizer(stop_words='english')
            filmes_df['genres'] = filmes_df['genres'].fillna('')  # Substituir valores nulos por strings vazias
            tfidf_matrix = tfidf.fit_transform(filmes_df['genres'])

            # Calcular a similaridade entre os filmes
            similaridade = pw.cosine_similarity(tfidf_matrix, tfidf_matrix)

            # Criar um DataFrame de similaridade
            similaridade_df = pd.DataFrame(similaridade, index=filmes_df['movieId'], columns=filmes_df['movieId'])

            # Obter os filmes assistidos pelo usuário
            filmes_assistidos = user_ratings['movieId'].tolist()

            # Calcular a pontuação de recomendação para cada filme
            recomendacoes = similaridade_df[filmes_assistidos].mean(axis=1).sort_values(ascending=False)

            # Remover os filmes já assistidos
            recomendacoes = recomendacoes[~recomendacoes.index.isin(filmes_assistidos)].head(10)

            # Adicionar informações dos filmes às recomendações
            recomendacoes_df = recomendacoes.reset_index()
            recomendacoes_df.columns = ['movieId', 'similarity_score']
            recomendacoes_df = recomendacoes_df.merge(filmes_df, on='movieId', how='left')

            return recomendacoes_df.to_dict(orient='records')
        except Exception as e:
            raise Exception(f"Erro ao gerar recomendações: {e}")
        
    async def filtragem_colaborativa(filmes: list, ratings: list, usuario_id: int) -> list:
        """
        Gera recomendações com base na filtragem colaborativa.
        """
        try:
            # Criar DataFrame de avaliações
            ratings_df = pd.DataFrame(ratings, columns=['userId', 'movieId', 'rating'])

            # Criar uma tabela de usuários x filmes
            user_movie_matrix = ratings_df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

            # Calcular similaridade entre usuários
            user_similarity = pw.cosine_similarity(user_movie_matrix)
            user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

            # Obter os filmes avaliados pelo usuário
            user_ratings = ratings_df[ratings_df['userId'] == usuario_id]
            if user_ratings.empty:
                return {"message": "Nenhum histórico de avaliações encontrado para o usuário."}

            # Obter os usuários mais similares
            similar_users = user_similarity_df[usuario_id].sort_values(ascending=False).index[1:6]

            # Obter os filmes avaliados pelos usuários similares
            similar_users_ratings = ratings_df[ratings_df['userId'].isin(similar_users)]

            # Calcular a média ponderada das avaliações dos usuários similares
            recomendacoes = similar_users_ratings.groupby('movieId')['rating'].mean().sort_values(ascending=False).head(10)

            # Adicionar informações dos filmes às recomendações
            filmes_df = pd.DataFrame(filmes, columns=['movieId', 'title', 'genres', 'year'])
            recomendacoes_df = recomendacoes.reset_index()
            recomendacoes_df.columns = ['movieId', 'collaborative_score']
            recomendacoes_df = recomendacoes_df.merge(filmes_df, on='movieId', how='left')

            return recomendacoes_df.to_dict(orient='records')
        except Exception as e:
            raise Exception(f"Erro ao gerar recomendações colaborativas: {e}")
        
    async def recomendacao_hibrida(filmes: list, ratings: list, usuario_id: int) -> list:
        """
        Gera recomendações híbridas combinando a função tratamento_usuario e filtragem colaborativa.
        """
        try:
            # Obter recomendações por conteúdo usando tratamento_usuario
            conteudo_recomendacoes = await TratamentoController.tratamento_usuario(filmes, ratings, usuario_id)

            # Obter recomendações colaborativas
            colaborativa_recomendacoes = await TratamentoController.filtragem_colaborativa(filmes, ratings, usuario_id)

            # Converter para DataFrames
            conteudo_df = pd.DataFrame(conteudo_recomendacoes)
            colaborativa_df = pd.DataFrame(colaborativa_recomendacoes)

            # Combinar os resultados com base no movieId
            hibrido_df = pd.merge(conteudo_df, colaborativa_df, on='movieId', how='outer')

            # Preencher valores ausentes com 0
            hibrido_df['similarity_score'] = hibrido_df['similarity_score'].fillna(0)
            hibrido_df['collaborative_score'] = hibrido_df['collaborative_score'].fillna(0)

            # Calcular uma pontuação final ponderada
            hibrido_df['final_score'] = (0.5 * hibrido_df['similarity_score']) + (0.5 * hibrido_df['collaborative_score'])

            # Substituir valores inválidos (NaN ou Infinity) por 0
            hibrido_df = hibrido_df.replace([float('inf'), float('-inf')], 0)
            hibrido_df = hibrido_df.fillna(0)

            # Selecionar apenas as colunas desejadas
            hibrido_df = hibrido_df[['movieId', 'title', 'genres', 'year', 'similarity_score', 'collaborative_score', 'final_score']]

            # Ordenar pelas pontuações finais
            hibrido_df = hibrido_df.sort_values(by='final_score', ascending=False).head(10)

            return hibrido_df.to_dict(orient='records')
        except Exception as e:
            raise Exception(f"Erro ao gerar recomendações híbridas: {e}")

    async def recomendacao_hibrida_conteudo(filmes: list, ratings: list, usuario_id: int) -> list:
        try:
            # Obter recomendações por conteúdo usando tratamento_usuario
            tratamento_recomendacoes = await TratamentoController.tratamento_usuario(filmes, ratings, usuario_id)

            # Obter recomendações por conteúdo usando filtragem_por_conteudo
            conteudo_recomendacoes = await TratamentoController.filtragem_por_conteudo(filmes, ratings, usuario_id)

            # Converter para DataFrames
            tratamento_df = pd.DataFrame(tratamento_recomendacoes)
            conteudo_df = pd.DataFrame(conteudo_recomendacoes)

            # Combinar os resultados com base no movieId
            hibrido_df = pd.merge(tratamento_df, conteudo_df, on='movieId', how='outer')

            # Preencher valores ausentes com 0
            hibrido_df['similarity_score'] = hibrido_df['similarity_score_x'].fillna(0)
            hibrido_df['content_score'] = hibrido_df['similarity_score_y'].fillna(0)
            # Calcular uma pontuação final ponderada
            hibrido_df['final_score'] = (0.5 * hibrido_df['similarity_score']) + (0.5 * hibrido_df['content_score'])

            # Substituir valores inválidos (NaN ou Infinity) por 0
            hibrido_df = hibrido_df.replace([float('inf'), float('-inf')], 0)
            hibrido_df = hibrido_df.fillna(0)

            # Selecionar apenas as colunas desejadas
            hibrido_df = hibrido_df[['movieId', 'title_x', 'title_y', 'genres_x', 'genres_y', 'year_x', 'year_y', 'similarity_score', 'content_score', 'final_score']]

            # Ordenar pelas pontuações finais
            hibrido_df = hibrido_df.sort_values(by='final_score', ascending=False).head(10)

            return hibrido_df.to_dict(orient='records')
        except Exception as e:
            raise Exception(f"Erro ao gerar recomendações híbridas: {e}")