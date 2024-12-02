# Projeto de Teste de Performance e Stress

Este projeto é uma aplicação para realizar testes de performance e stress em endpoints HTTP. Ele utiliza a biblioteca `locust` para testes de stress e `aiohttp` para testes de performance assíncronos.

## Estrutura do Projeto

- `Generators/`: Contém geradores de dados para os testes.
  - `CookieDataGenerator.py`: Gera dados fictícios para os testes.
- `Templates/`: Contém templates de requisições HTTP.
  - `CookieHttpTemplate.py`: Define ações HTTP para os testes.
- `PerformanceTest.py`: Implementa a lógica de execução dos testes de performance.
- `PerformanceTestInterface.py`: Define a interface para os testes de performance.
- `PerformanceTestLogger.py`: Logger para os resultados dos testes.
- `HttpRequestExecutor.py`: Executor de requisições HTTP.
- `StressTest.py`: Define os testes de stress utilizando `locust`.

## Executando os Testes de Stress

Para executar os testes de stress com `locust`, utilize o seguinte comando:
```sh
locust -f StressTest.py
```
Abra o navegador e acesse `http://localhost:8089` para configurar e iniciar os testes.

## Configuração dos Testes

Os testes podem ser configurados diretamente nos arquivos de template e geradores de dados. Edite os arquivos em `Generators/` e `Templates/` conforme necessário para ajustar os dados e as requisições.
