---
marp: true
theme: tokyonight
size: 16:9
paginate: true
header: ![width:120px](./images/miei.jpg)
footer: 'Inês Vicente (PG50436), Jorge Melo (PG50507), Miguel Martins (PG50655)'
---
<!-- _class: title -->
<!-- _paginate: false -->

# *Scripting* e Processamento de Linguagem Natural

## Análise de sentimentos em texto

---


# Funcionalidades

- Análise de sentimentos em *reviews* da *Amazon*

- Análise de sentimentos em *tweets* do *Twitter*
	- **Exemplo específico**: Análise de sentimentos em *tweets* sobre a *AI* e *ChatGPT* ao longo de uma conjunto de semanas

---

## *Reviews* da *Amazon*

- *Dataset* disponível no *Hugging Face*, com 6 idiomas diferentes: *Inglês*, *Francês*, *Alemão*, *Espanhol*, *Japonês* e *Chinês*.

- Tradução do texto não inglês para inglês, usando o modelo *Helsinki-NLP*, de forma a poder-se fazer a análise de sentimentos.

- Análise de sentimentos em cada *review*, usando o *NLTK*.


---

## *Tweets* segundo uma *query*

- Extrair *tweets* de acordo com uma *query* específica, usando o *Snscrape*.

- Análise de sentimentos em cada *tweet*, usando o *NLTK*.



---
<!-- _class: title -->
<!--- _paginate: false -->

# Módulos


---

![width:320px](images/hf.png) ![width:320px](images/nltk.png) ![width:320px](images/pandas.png) 

![width:220px center](images/twt.png)  ![width:420px center](images/streamlit.png)

---

## *Hugging Face*

- Usado para desenvolvimento de ferramentas de *Machine Learning*
- Usado para extrair *dataset* das reviews da *Amazon*
- Usado para traduzir o texto não inglês dos *datasets*
	- **Modelo**: *Helsinki-NLP*

---

## NLTK

- SIA (*SentimentIntensityAnalyzer*)
	- Usado para análise de sentimentos em texto

- Gera 4 indicadores:
	- *neg* - negativo
	- *neu* - neutro
	- *pos* - positivo
	- *compound* - composto


---

## Snscrape

- Usado para extrair *tweets* dando-se uma *query* específica


---

## Streamlit

- *Framework* para criação de *web apps* em *Python*
	- Possibilidade de criar *apps* com poucas linhas de código e sem conhecimentos de *web development* (*HTML*,*CSS*, *Javascript*, *DOM*, etc.)

- Bastante usado para visualização de dados estatísticos.


---


# *Web App* desenvolvida

- *Web App* desenvolvida com o *Streamlit*:

https://miguelamm42-sentimentanalysis-webapphome-riz5x5.streamlit.app/


---


<!--- _class: title --->

# Dúvidas?
## Obrigado!