

Projeto de Machine Learning para estimar o preco de mercado de residencias com base em caracteristicas como area, quantidade de quartos e idade da casa.

## Objetivo

Construir um modelo de regressao polinomial para prever o preco de residencias e disponibilizar uma estimativa a partir de dados informados pelo usuario no terminal.

## Tecnologias e bibliotecas

- Python 3
- pandas
- scikit-learn
- matplotlib
- seaborn
- openpyxl

## Estrutura do projeto

```text
RP_imoveis/
|-- dados.py            # limpeza e validacao dos dados
|-- modelo.py           # treino, avaliacao e previsao com regressao polinomial
|-- graficos.py         # geracao de graficos de diagnostico
|-- main.py             # orquestracao do pipeline
|-- residencias.xlsx    # base de dados utilizada
|-- requirements.txt    # dependencias do projeto
|-- .gitignore          # arquivos/pastas ignorados pelo Git
```

## Como funciona

1. Carrega a planilha `residencias.xlsx`.
2. Executa limpeza dos dados:
   - converte colunas para numerico;
   - remove valores negativos;
   - remove linhas com valores ausentes.
3. Separa variaveis de entrada e alvo (`preco`).
4. Aplica transformacao polinomial de grau 2.
5. Treina uma regressao linear sobre as features polinomiais.
6. Calcula previsoes no conjunto de teste.
7. Solicita dados do usuario no terminal e estima o preco de mercado.
8. Permite gerar graficos de analise (descomentando as linhas em `main.py`).

## Como executar

### 1) Clone o repositorio

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd RP_imoveis
```

### 2) Crie e ative ambiente virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

### 3) Instale as dependencias

```bash
pip install -r requirements.txt
```

### 4) Execute o projeto

```bash
python main.py
```

O programa pedira:
- area da casa;
- numero de quartos;
- idade da casa.

Depois disso, exibira no terminal a estimativa de preco.

## Geracao de graficos

O arquivo `main.py` possui chamadas comentadas para:
- grafico de residuos;
- real vs predito;
- histograma de residuos.

Basta descomentar as linhas para gerar os arquivos `.png`.

## Observacoes importantes

- A funcao em `modelo.py` calcula MAE e RMSE, mas a exibicao esta comentada. Se quiser destacar metricas no portfolio, descomente o `print` correspondente.

## Melhorias futuras

- separacao de modulo de treino e modulo de inferencia;
- salvar e carregar modelo treinado (`joblib`);
- testes automatizados para limpeza e previsao;
- pipeline com validacao cruzada e comparacao de modelos.

## Licenca

Defina uma licenca para o repositorio (por exemplo, MIT) antes da publicacao.
