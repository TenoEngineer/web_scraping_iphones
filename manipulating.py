import pandas as pd

class Manipulat:
    
    def __init__(self,df, list) -> None:
        self.df = df
        self.list = list

    def increment_GB(list, df):

        list_colors = ['Prata', 'PRATEADO', 'Cinza','Dourado','Ouro','Amarelo', 'PINK', 'SIERRA','Branco','Coral','Preto','Azul','Roxo','Verde','PRODUCT RED','Verde Meia-noite','GRAFITE','azul pacífico dourado','Rosa','meia-noite','estelar','Vermelho','AZUL-SIERRA']

        df['Title'] = df['Title'].str.replace('"', '', regex=True)
        df['Title'] = df['Title'].str.replace(', COM TELA DE 6,1, 5G,', '', regex=False)
        df['Title'] = df['Title'].str.replace(', COM TELA DE 6,1, 4G,', '', regex=False)

        for color in list_colors:
            df['Title'] = df['Title'].str.replace('(', '', regex=True)
            df['Title'] = df['Title'].str.replace(')', '', regex=True)
            df['Title'] = df['Title'].str.replace(str(color.upper()), '', regex=True)

        for gb in list:
            df['Title'] = df['Title'].str.replace('(', '', regex=True)
            df['Title'] = df['Title'].str.replace(')', '', regex=True)
            df['Title'] = df['Title'].str.replace(r'\s+', ' ', regex=True)  
            df['Title'] = df['Title'].str.replace('APPLE', '')
            df['Title'] = df['Title'].str.replace(' {}'.format(str(gb)), '-{}GB'.format(str(gb)), regex=True)      
        
    
    def finish(df):
        df['Title'] = df['Title'].str.upper()
        df['Title_Split'] = df['Title'].str.split('GB')
        df['Title'] = df['Title_Split'].str[0]
        df.drop(columns=['Title_Split'], inplace=True)
        df['Title_Split'] = df['Title'].str.split('TB')
        df['Title'] = df['Title_Split'].str[0]
        df.drop(columns=['Title_Split'], inplace=True)
    
    def export_csv(df):
        df['Title'] = df['Title'].str.replace(r'\s+', ' ', regex=True)
        df['Title'] = df['Title'].replace('PRO MAX 1', 'PRO MAX-1TB', regex=True)
        df['Title'] = df['Title'].replace('PRO 1', 'PRO-1TB', regex=True)
        df['Title'] = df['Title'].str.replace('4ª GERAÇÃO', '4', regex=True)
        df['Title'] = df['Title'].str.replace('3ª GERAÇÃO', '3', regex=True)
        df['Title'] = df['Title'].str.replace('2ª GERAÇÃO', '2', regex=True)
        df['Title'] = df['Title'].str.replace(' GERACAO', '', regex=True)
        df['Title'] = df['Title'].str.replace(' IPHONE', 'IPHONE', regex=True)
        df['Title'] = df['Title'].str.replace('GB ', 'GB', regex=True)
        df['Title'] = df['Title'].str.replace('PRODUCT', '', regex=True)
        df['Title'] = df['Title'].str.replace('™', '', regex=True)
        df['Title'] = df['Title'].str.replace('TELA DE 6,1, 5G,', '', regex=True)
        df['Title'] = df['Title'].str.replace('TELA DE 6,1, 4G,', '', regex=True)
        df['Title'] = df['Title'].str.replace('TELA DE 4,7, 4G,', '', regex=True)
        df['Title'] = df['Title'].str.replace('CELULAR', '', regex=True)
        df['Title'] = df['Title'].str.replace('SMARTPHONE', '', regex=True)
        df['Title'] = df['Title'].str.replace(' ,', '', regex=True)
        df['Title'] = df['Title'].str.replace(' -', '-', regex=True)
        df['Title'] = df['Title'].str.replace('--', '-', regex=True)
        df = df.drop_duplicates(subset=['Competitor', 'Title'], keep='last')
        
        excluir=['USADO', 'IPHONE 7', 'IPHONE 8', 'IPAD']
        for excluido in excluir:
            df = df[~df['Title'].str.contains(excluido)]
        df.to_csv("base.csv", sep=";", index=False)

if __name__ == '__main__':
    Manipulat