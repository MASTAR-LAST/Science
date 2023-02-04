class _AtomicError(Exception):
    """
    Exception raised for errors in the input salary.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="#"):
        self.message = message
        super().__init__(self.message)

class _UndefinedSymbolError(Exception):
    """
    Exception raised for errors in the input salary.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, symbol, message="The symbol is not exist :: Unsupported symbol -> "):
        self.message = message
        self.symbol = symbol
        super().__init__(self.message + str(self.symbol))


# import openai

# # استيراد مكتبة OpenAI

# # تعيين مفتاح API
# openai.api_key = "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"

# # العثور على نموذج لغة معين
# model_engine = "text-davinci-002"

# # التعريف على الإدخال والإخراج المطلوبين
# prompt = "What can you do?"

# # استدعاء API والحصول على الإجابة
# completion = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# # عرض الإجابة
# print(completion.choices[0].text)