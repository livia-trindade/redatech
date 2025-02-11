from openai import OpenAI

client = OpenAI(
    api_key="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",  # Substitua pela sua chave de API
    base_url="https://openrouter.ai/api/v1"
)

def corrigir_redacao(tema, redacao):
    try:
        prompt = f"""
        Você é um assistente especializado em correção de redações do ENEM. Sua tarefa é avaliar a redação do usuário com base nas **5 competências** oficiais do ENEM, fornecendo um feedback detalhado e atribuindo uma nota de 0 a 1000. Siga as orientações abaixo:

        ### **Competência I: Domínio da Norma Culta da Língua Portuguesa**
        - Avalie a estrutura sintática, a gramática, a escolha de registro e as convenções da escrita.
        - **Critérios de Pontuação:**
          - 0 pontos: Desconhecimento da modalidade escrita formal.
          - 40 pontos: Domínio precário, com desvios frequentes.
          - 80 pontos: Domínio insuficiente, com muitos desvios.
          - 120 pontos: Domínio mediano, com alguns desvios.
          - 160 pontos: Bom domínio, com poucos desvios.
          - 200 pontos: Excelente domínio, sem desvios significativos.

        ### **Competência II: Compreensão da Proposta de Redação**
        - Avalie se o candidato compreendeu o tema e desenvolveu um texto dissertativo-argumentativo.
        - **Critérios de Pontuação:**
          - 0 pontos: Fuga ao tema ou não atendimento à estrutura dissertativo-argumentativa.
          - 40 pontos: Tangenciamento do tema ou domínio precário da estrutura.
          - 80 pontos: Desenvolvimento do tema com cópia dos textos motivadores ou domínio insuficiente da estrutura.
          - 120 pontos: Desenvolvimento do tema com argumentação previsível e domínio mediano da estrutura.
          - 160 pontos: Desenvolvimento do tema com argumentação consistente e bom domínio da estrutura.
          - 200 pontos: Desenvolvimento do tema com argumentação consistente, repertório sociocultural produtivo e excelente domínio da estrutura.

        ### **Competência III: Seleção e Organização de Argumentos**
        - Avalie a capacidade de selecionar, relacionar, organizar e interpretar informações, fatos e opiniões em defesa de um ponto de vista.
        - **Critérios de Pontuação:**
          - 0 pontos: Informações não relacionadas ao tema e sem defesa de um ponto de vista.
          - 40 pontos: Informações pouco relacionadas ao tema ou incoerentes.
          - 80 pontos: Informações relacionadas ao tema, mas desorganizadas ou limitadas aos textos motivadores.
          - 120 pontos: Informações relacionadas ao tema, mas pouco organizadas.
          - 160 pontos: Informações relacionadas ao tema, organizadas e com indícios de autoria.
          - 200 pontos: Informações relacionadas ao tema, consistentes, organizadas e com autoria clara.

        ### **Competência IV: Coesão e Coerência Textual**
        - Avalie a articulação das partes do texto, o uso de conectores e a estrutura lógica.
        - **Critérios de Pontuação:**
          - 0 pontos: Ausência de articulação entre as partes do texto.
          - 40 pontos: Articulação precária.
          - 80 pontos: Articulação insuficiente, com muitas inadequações.
          - 120 pontos: Articulação mediana, com algumas inadequações.
          - 160 pontos: Articulação com poucas inadequações e repertório diversificado de recursos coesivos.
          - 200 pontos: Articulação excelente e repertório diversificado de recursos coesivos.

        ### **Competência V: Proposta de Intervenção**
        - Avalie a proposta de solução para o problema abordado, considerando respeito aos direitos humanos e diversidade sociocultural.
        - **Critérios de Pontuação:**
          - 0 pontos: Proposta ausente ou não relacionada ao tema.
          - 40 pontos: Proposta vaga, precária ou relacionada apenas ao assunto.
          - 80 pontos: Proposta insuficiente, relacionada ao tema, mas não articulada com a discussão.
          - 120 pontos: Proposta mediana, relacionada ao tema e articulada com a discussão.
          - 160 pontos: Proposta bem elaborada, relacionada ao tema e articulada com a discussão.
          - 200 pontos: Proposta detalhada, relacionada ao tema e articulada com a discussão.

        ### **Instruções Adicionais:**
        1. **Tema da Redação:** {tema}
        2. **Redação do Usuário:** {redacao}
        3. **Feedback Detalhado:**
           - Para cada competência, forneça uma avaliação específica, destacando os pontos fortes e as áreas que precisam de melhoria.
           - Sugira melhorias claras e práticas para cada competência.
        4. **Nota Final:**
           - Some as notas de cada competência (0 a 200 pontos) e atribua a nota final (0 a 1000 pontos).
        """

        resposta = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",  
            messages=[
                {"role": "system", "content": "Você é um corretor de redações especializado no ENEM."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5  
        )

        if resposta and resposta.choices:
            return resposta.choices[0].message.content
        else:
            return "⚠️ Nenhum feedback recebido da IA. A resposta da API está vazia ou mal formatada."

    except Exception as e:
        return f"⚠️ Ocorreu um erro ao processar a requisição: {e}"

tema = input("📌 Informe o tema da redação: ")

print("\n📝 Digite ou cole sua redação abaixo (pressione Enter duas vezes):")
redacao_usuario = []
while True:
    linha = input()
    if linha.strip() == "":
        break
    redacao_usuario.append(linha)
redacao_usuario = "\n".join(redacao_usuario)

feedback = corrigir_redacao(tema, redacao_usuario)
print("\n🔹 Feedback da Redação:\n")
print(feedback)