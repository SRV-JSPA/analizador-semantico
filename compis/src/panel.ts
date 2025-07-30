import * as vscode from 'vscode';

export class MyIDEPanel {
    public static show(context: vscode.ExtensionContext) {
        const panel = vscode.window.createWebviewPanel(
            'myIde',
            'Compilador',
            vscode.ViewColumn.One,
            {
                enableScripts: true
            }
        );

        panel.webview.html = MyIDEPanel.getHtml();

        panel.webview.onDidReceiveMessage(
            message => {
                if (message.command === 'run') {
                    vscode.window.showInformationMessage('Ejecutando compilador');
                }
            },
            undefined,
            context.subscriptions
        );
    }

    private static getHtml() {
        return `
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    font-family: sans-serif;
                    background-color: #1e1e1e;
                    color: #d4d4d4;
                    display: flex;
                    height: 100vh;
                }

                #sidebar {
                    width: 200px;
                    background-color: #252526;
                    padding: 10px;
                    box-sizing: border-box;
                    border-right: 1px solid #444;
                }

                #sidebar h3 {
                    margin-top: 0;
                    font-size: 14px;
                    color: #ccc;
                }

                #editor-area {
                    flex: 1;
                    display: flex;
                    flex-direction: column;
                }

                #toolbar {
                    background-color: #333;
                    padding: 10px;
                    border-bottom: 1px solid #444;
                }

                #editor {
                    flex: 1;
                    background-color: #1e1e1e;
                    color: #d4d4d4;
                    padding: 10px;
                    font-family: monospace;
                    font-size: 14px;
                    border: none;
                    resize: none;
                    outline: none;
                }

                #console {
                    background: #111;
                    color: #0f0;
                    padding: 10px;
                    height: 150px;
                    overflow-y: auto;
                    border-top: 1px solid #444;
                    font-family: monospace;
                    font-size: 13px;
                }

                button {
                    padding: 0.4em 1em;
                    background-color: #007acc;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 13px;
                }

                button:hover {
                    background-color: #005a9e;
                }
            </style>
        </head>
        <body>
            <div id="sidebar">
                <h3>Archivos</h3>
                <ul>
                    <li>main.txt</li>
                    <li>entrada.txt</li>
                    <li>codigo.ya</li>
                </ul>
            </div>

            <div id="editor-area">
                <div id="toolbar">
                    <button onclick="runCode()">Compilar</button>
                </div>

                <textarea id="editor" placeholder="Escribe tu código aquí..."></textarea>

                <div id="console">Consola lista...</div>
            </div>

            <script>
                const vscode = acquireVsCodeApi();
                function runCode() {
                    vscode.postMessage({ command: 'run' });
                    const consoleDiv = document.getElementById('console');
                    consoleDiv.innerText += "\\n>> Ejecutando compilador...";
                    consoleDiv.scrollTop = consoleDiv.scrollHeight;
                }
            </script>
        </body>
        </html>
        `;
    }
}
