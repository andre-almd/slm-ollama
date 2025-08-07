"""Script for prompt temaplte to test ollama models"""

#! ATTENTION:
# For small models like gemma3:1b, the parser might not work properly when
# using `parser.get_format_instructions()`, because these models often return
# the JSON schema itself instead of generating a response with actual
# example data.
#
# ✅ Better approach:
# Instead of relying on `get_format_instructions()`, explicitly include
# an example of the desired JSON output directly in the prompt, with realistic
# sample values.
#
# ❌ Avoid:
# Passing the raw format schema as an instruction — it leads to
# parsing failures.
#
# Example fix:
# Replace this —
#   "Return a JSON following this structure:\n{format_instructions}"
# With something like —
#   "Return a JSON like this:\n{ \"name\": \"João Silva\", \"age\": 30, ... }"

template = """
Você é um assistente que cria perfis fictícios de pessoas.
Crie um perfil de uma pessoa com base no tema: {tema}.

Retorne APENAS um JSON com os seguintes campos:
- name: nome completo (string)
- age: idade (número inteiro)
- profession: profissão (string)
- hobby: principal hobby (string)

Exemplo:
{{
  "name": "Carla Mendes",
  "age": 31,
  "profession": "Designer gráfica",
  "hobby": "Pintura digital"
}}
"""
