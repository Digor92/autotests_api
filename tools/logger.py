
import logging

def get_logger(name: str) ->logging.Logger:
    # Инициализация логгера с указанным именем
    logger = logging.getLogger(name)
    # Устанавливаем уровень логирования DEBUG для логгера,
    # чтобы он обрабатывал все сообщения от DEBUG и выше
    logger.setLevel(logging.DEBUG)
    # Создаем обработчик, который будет выводить логи в консоль
    handler = logging.StreamHandler()
    # Устанавливаем уровень логирования DEBUG для обработчика,
    # чтобы он обрабатывал все сообщения от DEBUG и выше
    handler.setLevel(logging.DEBUG)
    # Задаем форматирование лог-сообщений:
    # включаем время, имя логгера, уровень и сообщение
    formatter = logging.Formatter('%(asctime)s| %(name)s | %(levelname)s | %(message)s')
    # Применяем форматтер к обработчику
    handler.setFormatter(formatter)
    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    return logger

logger = get_logger("API_Client")
logger.info('Make POST request')
logger.info('Got 200 response')



