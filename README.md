> ## Autor:  Gabriel Zanoni Herculano [@GbrielZanoni](https://github.com/GbrielZanoni) 

## Estrutura do Projeto

```MD
├── books.csv            # Arquivo CSV gerado com os dados dos livros
├── driver.py            # Função para configurar o Selenium WebDriver
├── main.py              # Script principal que coordena o scraping
├── scraper.py           # Funções para coletar e extrair dados dos livros
├── writer.py            # Função para criar e escrever no CSV
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados pelo Git
├── __pycache__/         # Cache compilado do Python (ignorado)
```

## Descrição dos Arquivos e Funções

### `driver.py`

```python
def setup_driver(headless=True):
    """
    Inicializa e retorna o Chrome WebDriver.

    Parâmetros:
    - headless (bool): Se True, executa o navegador em modo invisível. (Bom para fazer a depuração, mas optei por deixar ligado para poupar tempo e processamento)

    Retorna:
    - selenium.webdriver.Chrome: instância do navegador configurada. Utilizado pelo código para interagir com o browser e obter seus valores
    """
```

---

### `main.py`

```python
def scrape_books():
    """
    Função principal que orquestra o processo de scraping:
    - Inicializa o driver.
    - Percorre as páginas da loja.
    - Coleta links dos livros com get_book_links().
    - Extrai dados com extract_book_info().
    - Salva os dados no arquivo CSV.
    """
```

---

### `scraper.py`

```python
def get_book_links(driver, page_url):
    """
    Coleta os links dos livros presentes em uma página.

    Parâmetros:
    - driver: instância do navegador Selenium - da função setup_driver
    - page_url (str): URL da página a ser analisada, como selecionar o botão da página (de ir para a próxima/anterior) é bem inviável, decidi iterar pelos índices (de 1 até 50) e mudando o URL de acordo com o processo, como: Pega os Livros, verifica a próxima págoina, vai para a próxima página, repete...

    Retorna:
    - list[str]: URLs dos livros encontrados. Itero um laço de repetição para obter todos os valores encontrados dentro de cada link.
    """

def extract_book_info(driver, book_url):
    """
    Extrai informações detalhadas de um livro. Optei por variar entre tags/CSS, o processo se assemelha a um XPath (processo utilizado para a extração de dados do Automation Anywhere, extremamente comum em web scraping)

    Parâmetros:
    - driver: instância do navegador Selenium.
    - book_url (str): URL da página do livro.

    Retorna:
    - dict: informações como nome, preço, disponibilidade, etc. A formatação já está bem definida e na ordem do .csv final  
    """
```

---

### `writer.py`

```python
def create_csv_file(filename):
    """
    Cria e prepara um arquivo CSV com cabeçalhos definidos.

    Parâmetros:
    - filename (str): nome do arquivo a ser criado.

    Retorna:
    - tuple: (objeto do arquivo aberto, csv.DictWriter configurado)
    """
```

```python
main.py
│
├──> setup_driver()                # (chama driver.py)
│     └── driver.py
│         └── Cria e retorna o WebDriver
│
├──> create_csv_file()            # (chama writer.py)
│     └── writer.py
│         └── Cria arquivo CSV e retorna o writer
│
└── LOOP por páginas
      ├──> get_book_links()       # (chama scraper.py)
      │     └── scraper.py
      │         └── Extrai links dos livros da página
      │
      └── LOOP por links de livros
             ├──> extract_book_info()   # (chama scraper.py)
             │     └── scraper.py
             │         └── Extrai informações detalhadas do livro
             │
             └──> writer.writerow()     # (usa o writer do writer.py)
```