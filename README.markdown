# Pain Point to Solution Agent Prototype

## Mô tả
Đây là prototype của một Pain Point to Solution Agent, được thiết kế để đề xuất các tính năng của Filum.ai phù hợp với các điểm đau của doanh nghiệp liên quan đến trải nghiệm khách hàng và dịch vụ khách hàng.

## Yêu cầu
- Python 3.8+
- Thư viện: `nltk`
- Dữ liệu NLTK: `punkt`, `stopwords`

## Cài đặt
1. Cài đặt thư viện:
   ```bash
   pip install nltk
   ```
2. Tải dữ liệu NLTK:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Cấu trúc thư mục
- `agent.py`: Mã nguồn chính của Agent.
- `features.json`: Cơ sở tri thức chứa thông tin về các tính năng của Filum.ai.
- `input.json` - Chứa mô tả điểm đau và ngữ cảnh doanh nghiệp để Agent xử lý.

## Cách chạy
1. Lưu `agent.py`, `input.json` và `features.json`  trong cùng thư mục.
2. Chạy script:
   ```bash
   python agent.py
   ```

## Ví dụ đầu vào
Thay đổi đầu vào trong `input.json` để mô tả pain point của doanh nghiệp. Ví dụ:

```json
{
  "pain_point": {
    "description": "We are struggling to collect customer feedback consistently after a purchase."
  },
  "business_context": {
    "industry": "retail",
    "channels": ["web", "POS"]
  }
}
```

## Ví dụ đầu ra
```json
{
  "pain_point_summary": "We are struggling to collect customer feedback consistently after a purchase.",
  "solutions": [
    {
      "feature_name": "voc_surveys_001",
      "module": "Automated Post-Purchase Surveys",
      "how_it_helps": "Automatically send surveys via email or SMS after each transaction to collect consistent customer feedback.",
      "relevance_score": 0.5,
      "more_info_link": "https://filum.ai/docs/voc-surveys"
    },
    {
      "feature_name": "voc_analysis_001",
      "module": "AI-Powered Topic & Sentiment Analysis",
      "how_it_helps": "Automatically extracts key topics and sentiment from open-ended survey responses and conversations.",
      "relevance_score": 0.333,
      "more_info_link": "https://filum.ai/docs/voc-analysis"
    }
  ]
}
```

## Hạn chế
- Hiện tại sử dụng phương pháp khớp từ khóa đơn giản. Có thể cải tiến bằng các mô hình NLP tiên tiến như BERT để hiểu toàn bộ câu và phân loại chính xác hơn.
- Chỉ sử dụng các tính năng đã được định nghĩa trong `features.json`. Cần cập nhật cơ sở tri thức khi có tính năng mới.
- Điểm phù hợp (`relevance_score`) được tính dựa trên các yếu tố đơn giản. Chưa dựa vào ngữ cảnh doanh nghiệp như: 
  - Quy mô doanh nghiệp
  - Ngành nghề
  - Kênh giao tiếp
  - Mức độ ưu tiên của pain point
