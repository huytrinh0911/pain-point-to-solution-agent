import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Chạy lần đầu cần download tài nguyên NLTK
nltk.download('punkt')
nltk.download('stopwords')

# ----------------------------
# Tải dữ liệu từ cơ sở tri thức
# ----------------------------
def load_knowledge_base(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# ----------------------------
# Trích xuất từ khóa từ văn bản
# ----------------------------
def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word.isalnum() and word not in stop_words]

# ----------------------------
# Tính điểm phù hợp giữa pain_point và một feature
# ----------------------------
def calculate_relevance(pain_point, feature):
    keywords = extract_keywords(pain_point['description'])
    total_keywords = len(keywords)

    if total_keywords == 0:
        return 0.0

    feature_keywords = feature.get('keywords', [])
    pain_points_covered = ' '.join(feature.get('pain_points_addressed', [])).lower()

    matches = [kw for kw in keywords if kw in feature_keywords or kw in pain_points_covered]
    score = len(matches) / total_keywords

    return round(score, 3)  # Làm tròn cho đẹp

# ----------------------------
# Agent chính: đưa ra danh sách giải pháp phù hợp
# ----------------------------
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


if __name__ == "__main__":
    knowledge_base = load_knowledge_base('features.json')
    input_data = json.load(open('input.json', 'r', encoding='utf-8'))
    result = get_solutions(input_data['pain_point'], knowledge_base)
    print(json.dumps(result, indent=2, ensure_ascii=False))
