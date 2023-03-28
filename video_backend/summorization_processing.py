from transformers import pipeline

def summorization(merged_list):
    summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
    summarization = []

    for item in merged_list:
        try:
            summary = summarizer(item)
            summarization.append(summary[0]['summary_text'])
        except IndexError:
            # Разбиваем строку на две части
            half = len(item) // 2
            first_half = item[:half]
            second_half = item[half:]
            # Запускаем обработку каждой половины
            first_summary = summarizer(first_half)
            second_summary = summarizer(second_half)
            # Склеиваем результаты
            summary = first_summary[0]['summary_text'] + second_summary[0]['summary_text']
            summarization.append(summary)

    return summarization
