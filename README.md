 # 🧠 Blind Assistance Device Using AI and Computer Vision

> 👁️ "Eyes might fail. This never will."  
A smart, AI-powered assistive system designed for visually impaired users. It provides real-time object detection, proximity alerts, and voice-based scene descriptions using just a webcam and speaker/headphones.

Team Project by:

- [Shaik Mohammed Asad](https://github.com/theshaikasad)
- [Revant Thakkar](https://github.com/Revant15)
---

## 🔍 Features

- ✅ Real-time object detection using MobileNet SSD
- 🎯 Proximity-based warnings with audio alerts
- 🗣️ Press a key to hear all detected objects in the frame
- 🎧 Works with Bluetooth headphones or speakers
- 🧠 Runs efficiently on low-power devices like Raspberry Pi

---

## 🎯 Use Case

This project helps visually impaired individuals understand their environment by identifying and announcing nearby objects and warning them when an object is dangerously close.

---

## 🧰 Components Used

- Raspberry Pi (or any Linux desktop)
- USB Webcam
- Bluetooth/Wired Speaker or Headphones
- Python 3.8+
- MobileNet SSD (Caffe model)
- Libraries: `opencv-python`, `pyttsx3`, `playsound`, `threading`

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/blind-assist-device.git
cd blind-assist-device

# Create virtual environment
python3 -m venv blind-env
source blind-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python blind_assist.py
```

- Press `Spacebar` to get a verbal list of all detected objects.
- The system will automatically **warn** if something is **too close** (e.g., a person or wall).
- Press `Q` to quit the program.

---

## 📷 Screenshots


```markdown
![Object Detection Frame](media/frame_demo.png)
```

> 📌 Recommended structure:
```
blind-assist-device/
│
├── blind_assist.py
├── requirements.txt
├── README.md
└── media/
    ├── frame_demo.png
    └── system_diagram.png
```

---

## 💡 Future Improvements

- Add GPS navigation integration
- Use YOLOv8-Nano for faster inference
- Implement voice command support
- Add obstacle avoidance using ultrasonic sensors

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
