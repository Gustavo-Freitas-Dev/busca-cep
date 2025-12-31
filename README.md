# BuscaCEP 🔎📍

Aplicação web simples desenvolvida com **Flask** para consulta de endereços a partir de um **CEP**, utilizando a API pública do **ViaCEP**.

O usuário informa um CEP válido e o sistema retorna os dados de endereço de forma clara e rápida.

---

## 🚀 Funcionalidades

- Consulta de CEP
- Validação de entrada (somente números, 8 dígitos)
- Integração com a API do ViaCEP
- Interface simples e funcional
- Backend organizado e fácil de manter

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- HTML
- CSS
- JavaScript
- ViaCEP API

---

## 📁 Estrutura do Projeto

```text
busca-cep/
│
├── app.py              # Aplicação Flask
├── viacep.py           # Integração com a API ViaCEP
├── validators.py       # Validação de CEP
│
├── templates/
│   └── index.html      # Página principal
│
├── static/
│   ├── css/
│   └── js/
│
├── requirements.txt
└── README.md
