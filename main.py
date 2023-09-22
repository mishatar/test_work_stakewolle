import requests
import base64
import json


def save_decoded_data_to_file(decoded_data, filename):
    ''' Функция для сохранения декодированных данных в файл. '''
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(decoded_data)
        print(f"Данные успешно записаны в файл: {filename}")
    except Exception as e:
        print(f"Произошла ошибка при записи данных в файл: {str(e)}")


def get_block_transactions_and_save_to_file(block_number, filename):

    api_url = f"https://www.mintscan.io/akash/block/{block_number}"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            block_data = response.json()

            if "txs" in block_data and "data" in block_data["txs"]:
                base64_data = block_data["data"]["txs"]
                decoded_data = base64.b64decode(*base64_data).decode('utf-8')

                save_decoded_data_to_file(decoded_data, filename)
            else:
                print("Данные о транзакциях в блоке не найдены.")
        else:
            print(f"Ошибка при запросе к API блокчейна. Код ответа: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка при выполнении запроса: {str(e)}")


if __name__=="__main__":
    block_number = 11260637
    output_filename = "decoded_data.txt"

    get_block_transactions_and_save_to_file(block_number, output_filename)