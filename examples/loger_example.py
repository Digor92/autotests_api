import logging

logger = logging.getLogger("AUTOTEST")
# Устанавливаем уровень логгирования на DEBUG, чтобы захватывать все сообщения
logger.setLevel(logging.DEBUG)

# Создаём консольный обработчик для вывода логов в консоль
hendler = logging.StreamHandler()
# Устанавливаем уровень для обработчика
hendler.setLevel(logging.DEBUG)

# Создаём форматтер для задания формата лог-сообщений
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
# Привязываем форматтер к обработчику
hendler.setFormatter(formatter)

# добавляем обработчик к логгеру
logger.addHandler(hendler)
# Примеры логирования с разными уровнями важности
logger.debug("Это сообщение уровня DEBUG.")  # Детальная информация для диагностики
logger.info("Это сообщение уровня INFO.")  # Сообщение для информирования о процессе
logger.warning("Это сообщение уровня WARNING.")  # Предупреждение о потенциальной проблеме
logger.error("Это сообщение уровня ERROR.")  # Сообщение об ошибке, программа продолжает работу
logger.critical("Это сообщение уровня CRITICAL.")  # Критическая ошибка, может вызвать остановку программы

