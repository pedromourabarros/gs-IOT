import cv2
import mediapipe as mp
import pygame
import time

# ------------------- CONFIGURAÇÕES -------------------
# Inicializar o som de alerta
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("alerta.mp3")  # Esse arquivo deve estar na mesma pasta

# Inicializar o MediaPipe para detectar mãos
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Criar o detector de mãos com alta confiança
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75
)

# Acessar a webcam
cap = cv2.VideoCapture(0)  # Use 0 para webcam padrão

# Variáveis de controle
alerta_ativo = False
ultimo_alerta = 0

# ------------------- LOOP PRINCIPAL -------------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao acessar a webcam.")
        break

    # Espelhar imagem e converter para RGB
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processar com MediaPipe
    result = hands.process(img_rgb)

    # Verificar se alguma mão foi detectada
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Desenhar a mão na imagem
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Verificar quais dedos estão abertos
            dedos_abertos = 0
            finger_tips = [8, 12, 16, 20]  # Pontas dos dedos (exceto polegar)

            for tip in finger_tips:
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                    dedos_abertos += 1

            # Se 4 ou mais dedos abertos, aciona o alerta
            if dedos_abertos >= 4:
                if not alerta_ativo or time.time() - ultimo_alerta > 3:
                    alerta_ativo = True
                    ultimo_alerta = time.time()
                    pygame.mixer.music.play()
                    print("⚠️ Gesto de emergência detectado!")

                # Mostrar alerta visual na tela
                cv2.putText(frame, "⚠️ EMERGENCIA DETECTADA", (30, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            else:
                alerta_ativo = False

    # Exibir a imagem com as anotações
    cv2.imshow("Sistema de Emergência - Detecção de Gesto", frame)

    # Sair ao pressionar ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ------------------- FINALIZAÇÃO -------------------
cap.release()
cv2.destroyAllWindows()
