
# 🖐️ Sistema de Detecção de Gesto para Situações de Emergência

## 📘 Descrição do Problema
Durante quedas de energia, a comunicação se torna limitada. Em locais como hospitais, residências com idosos ou pessoas com deficiência, pode ser difícil pedir ajuda. Pensando nisso, o projeto propõe uma forma alternativa e acessível de sinalizar uma emergência com um simples gesto.

## 💡 Visão Geral da Solução
Este projeto utiliza **Python**, **OpenCV**, **MediaPipe** e **Pygame** para detectar um gesto de "mão aberta" pela webcam. Ao reconhecer o gesto, o sistema:
- Exibe uma mensagem de alerta visual na tela
- Emite um som de alarme (`alerta.mp3`)
- Funciona offline, sem necessidade de conexão com a internet
- Pode ser executado até com a câmera do celular (via Iriun Webcam)

## ⚙️ Instruções de Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/pedromourabarros/gs-IOT.git
```

### 2. Criar ambiente virtual e ativar
```bash
python -m venv venv
.venv\Scriptsactivate
```

### 3. Instalar dependências
```bash
pip install mediapipe opencv-python pygame
```

### 4. Executar o sistema
```bash
python main.py
```

> ⚠️ Certifique-se de que o arquivo `alerta.mp3` esteja na mesma pasta do `main.py`.

---

## 🎥 Vídeo Demonstrativo

🔗 [Clique aqui para assistir no YouTube](https://www.youtube.com/SEU-LINK-AQUI)

---

## 🖼️ Figura de Funcionamento

Abaixo, uma captura do funcionamento do sistema:

![demonstração](https://github.com/pedromourabarros/gs-IOT/raw/main/image.png)

---

## 💻 Código Fonte

O código principal está no arquivo [`main.py`](./main.py), responsável por:

- Capturar vídeo da webcam
- Processar com MediaPipe para reconhecer a mão
- Detectar o gesto de emergência (mão aberta com 4 ou mais dedos)
- Exibir mensagem de alerta e tocar som via pygame

---

## 👥 Integrantes

- Pedro Moura Barros – RM550260  
- Rodrigo Fernandes dos Santos – RM98896  

---
