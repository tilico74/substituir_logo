# 📄 Substituir Logo em PDF

Ferramenta simples e eficiente desenvolvida em Python para substituir
automaticamente a logo de arquivos PDF.

Ideal para padronizar documentos como orçamentos, contratos e relatórios
de forma rápida e prática.

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   📂 Seleção de PDF por interface gráfica
-   🖼️ Substituição automática da logo
-   📌 Posicionamento configurável da imagem
-   💾 Geração de arquivo com nome único (timestamp)
-   📁 Salvamento automático na pasta Downloads
-   ⚡ Execução simples (duplo clique)

------------------------------------------------------------------------

## 🛠️ Tecnologias

-   Python 3
-   PyMuPDF (fitz)
-   Tkinter

------------------------------------------------------------------------

## 📁 Estrutura do Projeto

    substituir_logo/
    │
    ├── img/
    │   └── logo301x95.png
    │
    ├── main.py
    └── README.md

------------------------------------------------------------------------

## ▶️ Como usar

1.  Execute o arquivo:

``` bash
python main.py
```

2.  Selecione o arquivo PDF desejado

3.  O sistema irá:

    -   Substituir a logo
    -   Gerar um novo arquivo automaticamente

4.  O PDF final será salvo na pasta **Downloads**

------------------------------------------------------------------------

## ⚙️ Personalização

A posição da logo pode ser ajustada no código:

``` python
rect = fitz.Rect(x0, y0, x1, y1)
```

------------------------------------------------------------------------

## 💡 Possíveis melhorias

-   🔍 Detecção automática da logo
-   📦 Processamento em lote (múltiplos PDFs)
-   🌐 Interface web (Django ou Flask)
-   📊 Integração com sistemas de gestão

------------------------------------------------------------------------

## 🎯 Aplicações

-   Empresas de serviços
-   Imobiliárias
-   Construtoras
-   Escritórios administrativos

------------------------------------------------------------------------

## 👨‍💻 Autor

Desenvolvido por **Tilico**\
Projeto com foco em automação e produtividade 🚀
