# AI Text-to-3D Scene Generator

## 📌 Overview
This project converts user input text (sentence, paragraph, or document) into structured data that can be used to generate a 3D cartoon scene.

It uses:
- GPT-2 (optional) → enhance text
- spaCy NLP → extract meaning
- Scene Mapper → convert to 3D-ready data

---

## 🚀 Pipeline

User Input  
↓  
GPT-2 (Enhancement)  
↓  
spaCy NLP (Extract objects, actions, environment)  
↓  
Scene Mapper (Convert to 3D assets)  
↓  
3D Scene Output (Models + Animations + Environment)

---

## 🧠 Example

### Input:
```
A boy is playing football in a park. A dog is running on the road.
```

### NLP Output:
```
Scene 1: { "objects": ["boy", "football"], "actions": ["playing"], "environment": ["park"] }
Scene 2: { "objects": ["dog"], "actions": ["running"], "environment": ["road"] }
```

### 3D Output:
```
Scene 1: { "models": ["human_model", "ball_model"], "environment": ["park_scene"], "actions": ["play_animation"] }
Scene 2: { "models": ["dog_model"], "environment": ["road_scene"], "actions": ["run_animation"] }
```

---

## 🛠️ Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## ▶️ Run Project

```bash
python final_pipeline.py
```

---

## 📂 Project Structure

- `final_pipeline.py` → Main pipeline
- `nlp_extract.py` → NLP extraction
- `scene_mapper.py` → Mapping to 3D assets
- `gpt2_test.py` → GPT-2 testing

---

## 🎯 Key Concepts

- NLP converts text → structured data
- Scene mapper converts data → 3D assets
- GPT-2 enhances input (optional)

---

## 📌 Future Work

- Connect to Blender / Unity for real 3D rendering
- Improve object detection
- Add more animations and environments

---

## 👨‍💻 Author

SHAIK REHAN
