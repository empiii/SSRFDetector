# SSRF Detector

Esta extensão para o Burp Suite busca por parâmetros em solicitações POST que contenham matchs começando com "http" ou "https", indicando potenciais vulnerabilidades de SSRF (Server-Side Request Forgery) e Path Traversal através de requisção do parametro encontrado no body da requisição.

## Funcionalidades

- Identifica parâmetros suspeitos em solicitações POST.
- Permite a análise de potenciais vulnerabilidades SSRF e Path Traversal.
- Facilita a execução de Provas de Conceito (PoC) usando o BurpCollaborator.

## Utilização

1. Certifique-se de que a extensão esteja carregada no Burp Suite.
2. Envie solicitações POST através do Burp Proxy.
3. Verifique a saída na aba da extensão para encontrar parâmetros suspeitos.

## Instalação

1. Baixe o arquivo Jython (.jar) da extensão.
2. No Burp Suite, vá para "Extender" > "Extender Configurações".
3. Clique em "Add" e selecione o arquivo Jython (.jar) baixado.
4. A extensão será carregada e estará disponível no Burp Suite.
5. Caso não possua Request instalado, instale utilizando o comando. `# java -jar '/opt/BurpSuitePro/jython-standalone-2.7.3.jar' -m pip install requests`

## Melhorias Futuras

- Melhorar a detecção de parâmetros suspeitos.

# PoC

Utlizando ambiente SSRF labs - PortSwigger como Prova de Conceito.

https://github.com/empiii/SSRFDetector/assets/47393806/f48fc006-1323-45d5-8c03-dd511ce02330

