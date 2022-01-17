var partes = []

function gerar() {
    var text_return = '_\n'
    var text = document.getElementById('texto').value

    var break_line = 0
    var spaces = 0
    var break_line_r = 0

    for (var i = 0; i < text.length; i++) {
        if (text[i] === '\n') {
            break_line++;
        } else if (text[i] === '\r') {
            break_line_r++;
        } else if (text[i] === ' ') {
            spaces++;
        }
    }

    if (break_line > spaces && break_line > break_line_r) {
        text = text.split('\n')
    } else if (break_line_r > spaces && break_line_r > break_line) {
        text = text.split('\r')
    } else if (spaces > break_line && spaces > break_line_r) {
        text = text.split(' ')
    }

    for (var i = 0; i < text.length; i++) {
        if (text[i].length > 29) {
            text[i] = text[i].substring(0, 29)
        }
        text_return += text[i] + '\n'
        if (i % 6 == 0) {
            if (i != 0) {
                text_return += '_\n'
            }
        }
    }

    partes = text_return.split('_')
    partes.shift()

    const parent = document.getElementById("div-copiar")
    while (parent.firstChild) {
        parent.firstChild.remove()
    }


    for (var i = 0; i < partes.length; i++) {
        partes[i] = '_' + partes[i];

        var botao = document.createElement("div")
        botao.innerHTML = `<div class="col">
                <button class="btn btn-primary m-4" onclick="copiar(${i})">Copiar parte ${i + 1}</button>
            </div>`
        document.getElementById('div-copiar').appendChild(botao)
    }
    

    document.getElementById('textoConvertido').value = text_return

}

function copiar(i) {
    var cp = partes[i]
    const el = document.createElement('textarea');
    el.value = cp;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
}