# 🔎 BuscaCEP — Consulta de CEP com Flask

Aplicação web desenvolvida em **Flask** para consulta de endereços a partir de um **CEP brasileiro**, utilizando a API pública do **ViaCEP**.

O projeto segue princípios de **organização de código**, **separação de responsabilidades** e **validação de dados**, sendo uma aplicação simples, porém estruturada para fácil manutenção e evolução.

👉 **Aplicação em produção:**  
🔗 https://busca-cep-production-05f5.up.railway.app

---

## 🎯 Visão Geral

O **BuscaCEP** recebe um CEP informado pelo usuário, valida os dados de entrada, realiza a consulta na API do ViaCEP e retorna as informações de endereço de forma clara e objetiva.

O foco do projeto está em:
- Estrutura limpa de backend
- Código legível e modular
- Boas práticas no consumo de APIs externas
- Preparação para deploy em ambiente de produção

---

## 🧩 Arquitetura e Organização

O projeto foi estruturado para manter responsabilidades bem definidas:

- **app.py**  
  Responsável pela inicialização da aplicação Flask e definição das rotas.

- **validators.py**  
  Camada de validação de dados, garantindo que apenas CEPs válidos sejam processados.

- **viacep.py**  
  Camada de integração com a API externa, isolando chamadas HTTP e tratamento de respostas.

Essa separação facilita:
- Manutenção
- Testes futuros
- Evolução do projeto sem acoplamento excessivo

---

## 🚀 Funcionalidades

- Consulta de endereço a partir do CEP
- Validação de entrada (somente números e 8 dígitos)
- Consumo de API externa de forma segura
- Tratamento de erros para:
  - CEP inválido
  - CEP inexistente
  - Falhas de comunicação com a API
- Interface simples e funcional

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **HTML5**
- **CSS3**
- **JavaScript**
- **ViaCEP API**
- **Railway** (Deploy)

---

## 📁 Estrutura do Projeto

```text
busca-cep/
│
├── app.py              # Inicialização da aplicação e rotas
├── viacep.py           # Integração com a API ViaCEP
├── validators.py       # Regras de validação do CEP
│
├── templates/
│   └── index.html      # Interface da aplicação
│
├── static/
│   ├── css/            # Estilos
│   └── js/             # Scripts
│
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

## ⚙️ Execução Local

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/busca-cep.git
cd busca-cep
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
```
### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS
```bash
source venv/bin/activate
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar a aplicação
```bash
python app.py
```

### A aplicação estará disponível em:
```bash
http://127.0.0.1:5000
```

## 🌐 API Externa

**ViaCEP**

- API pública para consulta de endereços brasileiros
- Documentação oficial: https://viacep.com.br

---

## 🔍 Boas Práticas Aplicadas

- Separação de responsabilidades
- Validação de dados antes do processamento
- Código modular e legível
- Tratamento de erros
- Preparação para deploy em ambiente de produção

---

## 📈 Possíveis Evoluções

- Implementação de testes automatizados (pytest)
- Cache de consultas frequentes
- Interface mais responsiva
- Melhor feedback visual de erros
- Internacionalização (i18n)

---

## 👨‍💻 Autor

Desenvolvido por **Gustavo Freitas**  
**Backend Developer | Python**  

- Instagram: **@Gustavo.python**  
- LinkedIn: https://www.linkedin.com/in/gustavo-freitas-dev

