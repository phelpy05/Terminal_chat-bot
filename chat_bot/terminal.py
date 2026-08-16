# Licensed under the MIT License. See LICENSE file in the project root for full license information.

# terminal.py - interface de terminal para Vikir_mind
# chat no terminal usando a classe Vikir_mind (mind.py)

try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel
except ImportError:
    print("Erro: A biblioteca 'rich' nao esta instalada.")
    print("Instale com: pip install rich")
    exit(1)

import sys

# importa a classe de IA
from mind import Vikir_mind

# console do rich para output formatado
console = Console()


def imprimir_banner():
    # mostra o banner de boas-vindas
    console.print()
    console.print(
        Panel(
            '[bold cyan]Vikir[/bold cyan] - Assistente IA no Terminal\n'
            '[dim]Feito por Phelpy![/dim]',
            border_style='purple',
            padding=(1, 2),
        )
    )
    console.print()


def mostrar_comandos():
    # lista os comandos disponiveis
    console.print()
    console.print('[bold]Comandos disponiveis:[/bold]')
    comandos = [
        ('/sair, /exit, /quit', 'Sair do chat'),
        ('/clear, /limpar', 'Limpar historico da sessao'),
        ('/help, /ajuda, /?', 'Mostrar esta lista'),
        ('/model', 'Mostrar modelo atual'),
        ('/history, /historico', 'Mostrar tamanho do historico'),
    ]
    for cmd, desc in comandos:
        console.print(f'  [cyan]{cmd}[/cyan] -> {desc}')
    console.print()


def main():
    # loop principal do terminal
    imprimir_banner()
    mostrar_comandos()

    # cria a instancia da IA
    console.print('[dim]Inicializando Vikir...[/dim]')
    vikir = Vikir_mind()
    console.print('[green]Vikir pronto![/green]\n')

    # loop principal
    while True:
        try:
            # le input do usuario
            console.print('[bold violet]Você:[/bold violet] ', end='')
            entrada = input()

            # se vazio, pula
            if not entrada.strip():
                continue

            # verifica se é comando
            if entrada.strip().startswith('/'):
                comando = entrada.strip().lower()

                if comando in ('/sair', '/exit', '/quit'):
                    console.print('\n[dim]Até logo![/dim]')
                    break

                elif comando in ('/clear', '/limpar'):
                    # reinicia o chat - cria nova instancia
                    console.print('[yellow]Historico limpo![/yellow]')
                    vikir = Vikir_mind()
                    continue

                elif comando in ('/help', '/ajuda', '/?'):
                    mostrar_comandos()
                    continue

                elif comando == '/model':
                    console.print('[dim]Modelo: gemini-3.5-flash-lite[/dim]')
                    continue

                elif comando in ('/history', '/historico'):
                    console.print(
                        '[dim]Historico: 0 mensagens (uso de sessao)[/dim]'
                    )
                    continue

                else:
                    console.print(f'[red]Comando desconhecido: {comando}[/red]')
                    continue

            # envia para o Vikir pensar
            console.print('[dim]Vikir esta pensando...[/dim]')
            resposta = vikir.pensar(entrada)

            # imprime a resposta
            console.print()
            if resposta:
                # tenta renderizar como markdown se for texto simples
                try:
                    console.print(Markdown(resposta))
                except Exception:
                    console.print(resposta)
            else:
                console.print('[red]Vikir não respondeu. Tente novamente.[/red]')

            console.print()

        except KeyboardInterrupt:
            console.print('\n[dim]Interrompido. Até logo![/dim]')
            break
        except Exception as e:
            console.print(f'\n[red]Erro: {e}[/red]')
            console.print(
                '[dim]Tente novamente ou usa /sair para sair.[/dim]'
            )
            continue

    console.print('\n[dim]Obrigado por usar Vikir![/dim]')


if __name__ == '__main__':
    main()
