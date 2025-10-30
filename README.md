README

Título
Fila de Triagem Manchester

Descrição
Aplicação de linha de comando para simular uma fila de triagem baseada no protocolo Manchester, permitindo registrar pacientes, executar perguntas de classificação e organizar o atendimento conforme prioridade médica. O sistema permite registrar nome, prioridade e respostas do paciente, listar a fila e realizar atendimentos sequenciais.

Estrutura dos arquivos
main.py: Arquivo principal, responsável pelo loop do menu e operação da aplicação.

menu.py: Implementa o menu de interação, triagem, visualização da fila e atendimento de paciente.

fila.py: Implementa a estrutura de fila utilizando deque, gestão dos pacientes registrados.

paciente.py: Define o objeto paciente, seus atributos e representação textual.

arvore.py: Lógica da árvore de triagem (Manchester), perguntas e classificação por cor (prioridade).

Requisitos
Python 3.7+

Pip (gerenciador de pacotes)

Nenhuma biblioteca externa é requerida

Como executar
Crie e ative um ambiente virtual (opcional):

bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\\Scripts\\activate    # Windows
Instale dependências:

bash
pip install -r requirements.txt
Execute a aplicação:

bash
python main.py
Funcionalidades
Registro de paciente por triagem Manchester

Visualização de pacientes na fila

Atendimento sequencial dos pacientes

Priorização automática por cor do protocolo Manchester

requirements.txt

text
# Nenhum pacote externo requerido
Se desejar adicionar dependências externas no futuro, basta incluí-las neste arquivo.

Se precisar dos arquivos gerados (.md ou .txt), avise qual formato prefere.
