# Painel Comercial · Ibacem Agrícola

Protótipo de **painel comercial para o mercado interno brasileiro**, construído para a
**Ibacem Agrícola** — produtora e exportadora de **manga e uva** do Vale do São Francisco,
com 40 anos de história e presença em mais de 20 países.

## 🔗 Acessar o painel

**https://broontreyer.github.io/ibacem-painel/**

> Abre com uma breve animação da marca (com áudio) e segue para o painel.

## O que o painel mostra

- **Resumo executivo** — faturamento, volume, margem bruta, ticket médio e **meta do mês** (com projeção de fechamento) + indicadores operacionais.
- **Acompanhamento de vendas** — faturamento acumulado vs. meta, evolução mensal (ano a ano) e vendas diárias por produto.
- **Desempenho comercial** — por UF, por canal, por cliente e por variedade.
- **Rentabilidade & preço** — evolução do preço médio e frete por UF (R$/kg, por distância da origem).
- **Estoque & logística** — posição e cobertura em dias.
- **Qualidade comercial** — devolução, desconto comercial e inadimplência.
- **Filtros interativos** (produto, UF, canal, cliente) · **modo escuro**.

## Observações

- **Dados demonstrativos (fictícios)**, construídos para serem coerentes entre si
  (faturamento = volume × preço, margem, ticket, cobertura de estoque, etc.).
- Protótipo de demonstração — **Inteligência de Mercado**.

## Estrutura

```
index.html          painel (abre direto)
ibacem-intro.mp4    vídeo de abertura
ibacem-logo.png     logo
fonte/              código-fonte editável + gerador
```
