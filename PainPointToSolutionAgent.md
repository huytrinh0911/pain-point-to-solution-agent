# Tài liệu thiết kế: Pain Point to Solution Agent

## 1. Định nghĩa đầu vào của Agent

### Thông tin cần thiết

Để hiểu và phân tích hiệu quả các điểm đau (pain points) của doanh nghiệp, Agent cần thu thập các thông tin sau:

- **Mô tả điểm đau**: Một đoạn văn bản ngắn gọn mô tả vấn đề doanh nghiệp đang gặp phải liên quan đến trải nghiệm khách hàng (CX) hoặc dịch vụ khách hàng (CS).
- **Ngữ cảnh doanh nghiệp** (tùy chọn): Quy mô doanh nghiệp (nhỏ, vừa, lớn), ngành nghề (bán lẻ, giáo dục, tài chính, v.v.), và các kênh tương tác chính (web, mobile, mạng xã hội, v.v.).
- **Mức độ ưu tiên**: Mức độ nghiêm trọng của vấn đề (thấp, trung bình, cao) hoặc mục tiêu cụ thể (tăng hiệu quả, giảm chi phí, cải thiện trải nghiệm khách hàng).
- **Kênh tương tác bị ảnh hưởng**: Các kênh cụ thể nơi điểm đau xảy ra (ví dụ: email, chat, POS, v.v.).

### Cấu trúc và định dạng đầu vào

Đầu vào được thiết kế dưới dạng JSON để đảm bảo tính cấu trúc, dễ xử lý và mở rộng. Định dạng JSON được chọn vì:

- Dễ tích hợp với các hệ thống hiện đại (API, CRM, v.v.).
- Cho phép xác định các trường bắt buộc và tùy chọn.
- Hỗ trợ xử lý tự động trong Python.

**Cấu trúc JSON đầu vào**:

```json
{
  "pain_point": {
    "description": "string", // Mô tả điểm đau (bắt buộc)
  },
  "business_context": {
    "industry": "string", // Ngành nghề (tùy chọn)
    "channels": ["string"] // Các kênh bị ảnh hưởng (tùy chọn)
  }
}
```

**Ví dụ đầu vào**:

```json
{
  "pain_point": {
    "description": "Chúng tôi gặp khó khăn trong việc thu thập phản hồi khách hàng một cách nhất quán sau khi mua hàng.",
  },
  "business_context": {
    "industry": "bán lẻ",
    "channels": ["web", "POS"]
  }
}
```

### Lý do thiết kế

- **Mô tả điểm đau**: Là thông tin cốt lõi để Agent xác định vấn đề cần giải quyết.
- **Ngữ cảnh doanh nghiệp**: Giúp Agent cá nhân hóa giải pháp phù hợp với đặc thù doanh nghiệp.
- **Mức độ ưu tiên**: Hỗ trợ Agent ưu tiên các giải pháp có tác động cao nhất.
- **Kênh tương tác**: Giúp xác định các tính năng của Filum.ai liên quan đến kênh cụ thể (ví dụ: khảo sát qua Zalo, SMS).

---

## 2. Định nghĩa đầu ra của Agent

### Cách trình bày giải pháp

Agent sẽ trả về danh sách các giải pháp của Filum.ai phù hợp với điểm đau được mô tả. Mỗi giải pháp sẽ bao gồm thông tin chi tiết để người dùng hiểu rõ cách áp dụng và giá trị mang lại. Đầu ra được trình bày dưới dạng JSON để đảm bảo tính cấu trúc và dễ tích hợp với các hệ thống khác (ví dụ: giao diện người dùng, CRM).

### Cấu trúc và định dạng đầu ra

**Cấu trúc JSON đầu ra**:

```json
{
  "pain_point_summary": "string", // Tóm tắt điểm đau được phân tích
  "solutions": [
    {
      "feature_name": "string", // Tên tính năng của Filum.ai
      "module": "string", // Tên mô-đun hoặc tính năng
      "how_it_helps": "string", // Mô tả cách tính năng giải quyết điểm đau
      "relevance_score": float, // Điểm phù hợp (0.0 - 1.0)
      "link_to_docs": "string" // Liên kết đến tài liệu chi tiết
    }
  ]
}
```

**Ví dụ đầu ra**:

```json
{
  "pain_point_summary": "Khó khăn trong việc thu thập phản hồi khách hàng nhất quán sau khi mua hàng qua web và POS.",
  "solutions": [
    {
      "feature_name": "voc_surveys_001",
      "module": "Automated Post-Purchase Surveys",
      "how_it_helps": "Tự động gửi khảo sát qua email hoặc SMS sau mỗi giao dịch để thu thập phản hồi khách hàng một cách nhất quán.",
      "relevance_score": 0.95,
      "link_to_docs": "https://filum.ai/docs/voc-surveys"
    }
  ]
}
```

### Thông tin cần bao gồm

- **Tóm tắt điểm đau**: Xác nhận rằng Agent đã hiểu đúng vấn đề.
- **Tên tính năng**: Rõ ràng, ngắn gọn, dễ nhận diện.
- **Mô tả**: Giải thích cách tính năng giải quyết điểm đau, nhấn mạnh giá trị cụ thể.
- **Điểm phù hợp**: Đánh giá mức độ liên quan của giải pháp (dựa trên từ khóa, kênh, và ngữ cảnh).
- **Danh mục**: Giúp người dùng hiểu tính năng thuộc nhóm nào trong Filum.ai.
- **Kênh hỗ trợ**: Chỉ ra các kênh mà tính năng có thể áp dụng.
- **Liên kết tài liệu**: Cung cấp nguồn tham khảo để người dùng tìm hiểu thêm.

### Lý do thiết kế

- **Cấu trúc JSON**: Dễ dàng tích hợp với các hệ thống khác và hiển thị trên giao diện người dùng.
- **Điểm phù hợp**: Giúp người dùng ưu tiên giải pháp tốt nhất khi có nhiều lựa chọn.
- **Liên kết tài liệu**: Khuyến khích người dùng tìm hiểu sâu hơn để triển khai giải pháp.

---

## 3. Thiết kế cấu trúc Feature Knowledge Base

### Cách biểu diễn tính năng của Filum.ai

Cơ sở tri thức (Knowledge Base) lưu trữ thông tin về các tính năng của Filum.ai sẽ được tổ chức dưới dạng JSON, vì:

- JSON dễ đọc, dễ bảo trì và hỗ trợ tích hợp với Python.
- Cho phép lưu trữ các thuộc tính phức tạp như danh sách kênh, từ khóa, và mô tả.
- Phù hợp để tra cứu nhanh và tìm kiếm dựa trên từ khóa.

### Cấu trúc cơ sở tri thức

**Cấu trúc JSON**:

```json
[
  {
    "feature_id": "string", // Mã định danh duy nhất
    "module": "string", // Tên tính năng
    "category": "VoC|AI Customer Service|Insights|Customer 360|AI & Automation", // Danh mục
    "description": "string", // Mô tả tính năng
    "pain_points_addressed": ["string"], // Danh sách điểm đau mà tính năng giải quyết
    "keywords": ["string"], // Từ khóa liên quan để tìm kiếm
    "channels_supported": ["string"], // Các kênh được hỗ trợ
    "link_to_docs": "string" // Liên kết đến tài liệu
  }
]
```

**Ví dụ cơ sở tri thức**:

```json
[
  {
    "feature_id": "voc_surveys_001",
    "module": "Automated Post-Purchase Surveys",
    "category": "VoC - Surveys",
    "description": "Tự động gửi khảo sát qua email hoặc SMS sau mỗi giao dịch để thu thập phản hồi khách hàng một cách nhất quán.",
    "pain_points_addressed": [
      "Khó khăn trong việc thu thập phản hồi khách hàng nhất quán",
      "Không đủ dữ liệu để đo lường mức độ hài lòng"
    ],
    "keywords": ["survey", "feedback", "post-purchase", "customer satisfaction"],
    "channels_supported": ["web", "POS", "email", "SMS"],
    "link_to_docs": "https://filum.ai/docs/voc-surveys"
  },
  {
    "feature_id": "ai_inbox_001",
    "module": "AI Agent for FAQ & First Response",
    "category": "AI Customer Service - AI Inbox",
    "description": "AI tự động trả lời các câu hỏi thường gặp, giảm tải cho nhân viên và cung cấp phản hồi tức thì.",
    "pain_points_addressed": [
      "Nhân viên hỗ trợ bị quá tải bởi các câu hỏi lặp lại",
      "Thời gian phản hồi khách hàng quá lâu"
    ],
    "keywords": ["AI agent", "FAQ", "automation", "response time"],
    "channels_supported": ["chat", "email", "Zalo"],
    "link_to_docs": "https://filum.ai/docs/ai-inbox"
  }
]
```

### Các thuộc tính cần thiết

- **feature_id**: Định danh duy nhất để quản lý và tra cứu.
- **module**: Tên tính năng, dễ hiểu và ngắn gọn.
- **category**: Phân loại tính năng theo danh mục sản phẩm của Filum.ai.
- **description**: Mô tả cách tính năng hoạt động và giá trị mang lại.
- **pain_points_addressed**: Danh sách các điểm đau cụ thể mà tính năng có thể giải quyết.
- **keywords**: Từ khóa giúp khớp với mô tả điểm đau của người dùng.
- **channels_supported**: Các kênh mà tính năng hỗ trợ, giúp lọc giải pháp theo ngữ cảnh.
- **link_to_docs**: Liên kết đến tài liệu chi tiết.

### Lý do thiết kế

- **Danh sách điểm đau và từ khóa**: Hỗ trợ tìm kiếm và khớp dựa trên nội dung đầu vào.
- **Kênh hỗ trợ**: Đảm bảo giải pháp phù hợp với các kênh mà doanh nghiệp sử dụng.
- **JSON đơn giản**: Dễ dàng mở rộng khi Filum.ai bổ sung tính năng mới.

---

## 4. Logic cốt lõi và phương pháp khớp (Matching Approach)

### Tổng quan logic

Agent sử dụng phương pháp **tìm kiếm dựa trên từ khóa và ngữ cảnh** kết hợp với **điểm phù hợp (relevance score)** để đề xuất giải pháp. Quy trình xử lý bao gồm:

1. **Phân tích đầu vào**: Trích xuất từ khóa từ mô tả điểm đau và ngữ cảnh doanh nghiệp.
2. **Khớp với cơ sở tri thức**: So sánh từ khóa và kênh bị ảnh hưởng với các thuộc tính trong cơ sở tri thức.
3. **Tính điểm phù hợp**: Sử dụng một công thức đơn giản để đánh giá mức độ liên quan của mỗi tính năng.
4. **Sắp xếp và trả kết quả**: Trả về danh sách các giải pháp, ưu tiên các giải pháp có điểm phù hợp cao nhất.

### Chi tiết phương pháp khớp

1. **Trích xuất từ khóa**:
   - Sử dụng thư viện xử lý ngôn ngữ tự nhiên (NLP) như `nltk` hoặc `spacy` để trích xuất từ khóa từ mô tả điểm đau.
   - Ví dụ: Với điểm đau "Khó khăn trong việc thu thập phản hồi khách hàng nhất quán sau khi mua hàng", từ khóa có thể là: \["feedback", "survey", "post-purchase", "consistent"\].
2. **So sánh từ khóa**:
   - Tính số lượng từ khóa từ mô tả điểm đau khớp với `keywords` và `pain_points_addressed` của mỗi tính năng.
   - Tính tỷ lệ khớp kênh: Số lượng kênh trong đầu vào khớp với `channels_supported`.
3. **Tính điểm phù hợp**:
   - Công thức:\
     `relevance_score = keyword_match_ratio)`
     - `keyword_match_ratio`: Tỷ lệ từ khóa khớp (số từ khóa khớp / tổng số từ khóa).
     <!-- - `channel_match_ratio`: Tỷ lệ kênh khớp (số kênh khớp / tổng số kênh trong đầu vào). -->
     <!-- - `severity_weight`: Điểm dựa trên mức độ nghiêm trọng (low: 0.3, medium: 0.6, high: 1.0). -->
4. **Lọc và sắp xếp**:
   - Chỉ trả về các giải pháp có `relevance_score` &gt; 0.3.
   - Sắp xếp theo `relevance_score` giảm dần.

### Lý do thiết kế

- **Tìm kiếm dựa trên từ khóa**: Đơn giản, hiệu quả, phù hợp với prototype.
<!-- - **Kết hợp ngữ cảnh kênh**: Đảm bảo giải pháp phù hợp với các kênh mà doanh nghiệp sử dụng. -->
- **Điểm phù hợp**: Cung cấp cách đánh giá khách quan để ưu tiên giải pháp tốt nhất.
- **Khả năng mở rộng**: Có thể cải tiến bằng cách sử dụng các mô hình **NLP tiên tiến (như BERT)** để hiểu được toàn bộ nội dung câu và phân loại pain_points.

---

## 5. Prototype triển khai (Python)

Dưới đây là mô tả về prototype triển khai bằng Python, sử dụng cơ sở tri thức mẫu và logic khớp đã nêu.

### Cấu trúc prototype

- **Tệp chính**: `agent.py` - Chứa logic chính của Agent.
- **Tệp cơ sở tri thức**: `features.json` - Lưu trữ thông tin về các tính năng của Filum.ai.
- **Tệp đầu vào**: `input.json` - Chứa mô tả điểm đau và ngữ cảnh doanh nghiệp để Agent xử lý.
- **Thư viện sử dụng**:
  - `json`: Xử lý đầu vào và cơ sở tri thức.
  - `nltk`: Phân tích từ khóa từ mô tả điểm đau.


<!-- ### Cách chạy prototype

1. Cài đặt các thư viện:

   ```bash
   pip install nltk
   ```

2. Tải dữ liệu NLTK:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

3. Chạy script:

   ```bash
   python agent.py
   ``` -->

### Import các thư viện cần thiết

Dưới đây là mã nguồn của prototype, được lưu trong tệp `agent.py`:

```python
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
```

### Tải dữ liệu từ cơ sở tri thức

```python
def load_knowledge_base(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
```

### Trích xuất từ khóa từ văn bản
```python
def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word.isalnum() and word not in stop_words]
```

### Tính điểm phù hợp cho một tính năng
```python
def calculate_relevance(pain_point, feature):
    keywords = extract_keywords(pain_point['description'])
    total_keywords = len(keywords)

    if total_keywords == 0:
        return 0.0
    feature_keywords = feature.get('keywords', [])
    pain_points_covered = ' '.join(feature.get('pain_points_addressed', [])).lower()

    matches = [kw for kw in keywords if kw in feature_keywords or kw in pain_points_covered]
    score = len(matches) / total_keywords

    return round(score, 3)
```


### Xử lý đầu vào và trả về giải pháp
```python
def get_solutions(pain_point, knowledge_base, threshold=0.3):
    ranked = []

    for feature in knowledge_base:
        score = calculate_relevance(pain_point, feature)
        if score >= threshold:
            ranked.append({
                "feature_name": feature['feature_id'],
                "module": feature['module'],
                "how_it_helps": feature['description'],
                "relevance_score": score,
                "more_info_link": feature.get('link_to_docs', '')
            })

    # Sắp xếp theo điểm phù hợp giảm dần
    ranked.sort(key=lambda x: x['relevance_score'], reverse=True)
    return {
            "pain_point_summary": pain_point['description'],
            "solutions": ranked
            }
```

### Hàm chính
```python
if __name__ == "__main__":
    knowledge_base = load_knowledge_base('features.json')
    input_data = json.load(open('input.json', 'r', encoding='utf-8'))
    result = get_solutions(input_data['pain_point'], knowledge_base)
    print(json.dumps(result, indent=2, ensure_ascii=False))
```


### Đầu vào mẫu
```json
{
  "pain_point": {
    "description": "We have no clear idea which customer touchpoints are causing the most frustration."
  },
  "business_context": {
    "industry": "retail",
    "channels": ["web", "POS"]
  }
}
```

### Kết quả
```text
{
  "pain_point_summary": "We have no clear idea which customer touchpoints are causing the most frustration.",
  "solutions": [
    {
      "feature_name": "insights_experience_001",
      "module": "Customer Journey Experience Analysis",
      "how_it_helps": "Identifies friction points by analyzing feedback and operational data across the customer journey.",
      "relevance_score": 0.667,
      "more_info_link": "https://filum.ai/docs/insights-experience"
    }
  ]
}
```