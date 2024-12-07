
# **Sistema de Detecção de Fraudes com Machine Learning**

Bem-vindo ao projeto **Sistema de Detecção de Fraudes**, um aplicativo interativo desenvolvido para identificar transações fraudulentas em tempo real usando técnicas avançadas de aprendizado de máquina. Este projeto utiliza o modelo **Isolation Forest**, uma abordagem não supervisionada para detectar anomalias em grandes conjuntos de dados.

### 🌐 **Acesse a Aplicação Web**
Acesse o aplicativo diretamente via este link: [**Detecção de Fraudes**](https://deteccao-de-fraude-4neytyurzkkusx38a6dhcu.streamlit.app/)

---

## **Índice**
- [Descrição do Projeto](#descrição-do-projeto)
- [Recursos do Projeto](#recursos-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto Localmente](#como-executar-o-projeto-localmente)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)

---

## **Descrição do Projeto**

Este sistema foi desenvolvido para:
- Demonstrar como um modelo de aprendizado de máquina pode ser aplicado na detecção de fraudes financeiras.
- Fornecer uma interface interativa para simular transações fraudulentas e legítimas.
- Explicar visualmente o funcionamento do modelo através de métricas e resultados em tempo real.

O sistema utiliza o modelo **Isolation Forest** para identificar anomalias em transações financeiras, classificando-as como fraudulentas ou não fraudulentas.

---

## **Recursos do Projeto**

- **Interface de Usuário:**
  - Desenvolvida em **Streamlit**, com design customizado para facilitar a usabilidade.
  - Simulação de transações com botões interativos.

- **Detecção em Tempo Real:**
  - Permite classificar transações simuladas diretamente na aplicação.

- **Métricas de Avaliação:**
  - Mostra métricas como precisão, recall e F1-Score para validar a performance do modelo.

- **Engenharia de Features:**
  - Geração de variáveis para aprimorar a detecção, como:
    - Contagem de transações por dispositivo.
    - Número de dispositivos associados a comerciantes.
    - Intervalos de tempo entre transações.

- **Simulação de Transações:**
  - Gera dados fictícios para avaliar a performance do modelo em condições controladas.

---

## **Tecnologias Utilizadas**

- **Linguagem:** Python
- **Bibliotecas:**
  - Streamlit (para interface web)
  - Scikit-learn (para o modelo Isolation Forest)
  - Pandas e NumPy (para manipulação de dados)
  - Matplotlib (para visualizações no notebook)
- **Modelo de Machine Learning:**
  - Isolation Forest (para detecção de anomalias)

---

## **Como Contribuir**

Contribuições são sempre bem-vindas! Para contribuir:
1. Fork este repositório.
2. Crie uma branch para a sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça as alterações necessárias e commit:
   ```bash
   git commit -m "Adiciona minha nova feature"
   ```
4. Envie para o repositório principal:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## **Licença**

Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
