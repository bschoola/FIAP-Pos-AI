# FIAP-Pos-AI

Este repositório contém materiais e projetos da Pós-Graduação em Inteligência Artificial da FIAP.

## Estrutura do Repositório

Cada aula possui sua própria pasta com conteúdo específico.

## Aula 3: Introdução às Redes Neurais com PyTorch

### Descrição
Esta aula apresenta um exemplo prático de implementação de uma rede neural simples usando PyTorch para resolver um problema de regressão. O modelo é treinado para prever o tempo de conclusão de uma tarefa baseado em uma entrada numérica (ex.: unidades de trabalho).

### Conteúdo
- `run.py`: Script principal que define, treina e testa a rede neural.
- `requirements`: Arquivo com as dependências necessárias (PyTorch).

### Como Executar
1. Instale as dependências:
   ```
   pip install -r Aula3/requirements
   ```
2. Execute o script:
   ```
   python Aula3/run.py
   ```

O script treinará a rede por 1000 épocas e exibirá o progresso a cada 100 épocas. No final, fará uma previsão para uma entrada de teste (10.0) e mostrará o resultado em minutos.

### Conceitos Abordados
- Definição de uma rede neural com camadas lineares e ativação ReLU.
- Treinamento usando gradiente descendente estocástico (SGD).
- Cálculo de perda com erro quadrático médio (MSE).
- Previsão com dados não vistos.