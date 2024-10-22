import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark App")  


        # Create widgets
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)  


        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.watermark_text_label = tk.Label(root, text="Enter watermark text:")
        self.watermark_text_label.pack(pady=5)

        self.watermark_text_entry = tk.Entry(root)
        self.watermark_text_entry.pack(pady=5)

        self.apply_watermark_button = tk.Button(root, text="Apply Watermark", command=self.apply_watermark)
        self.apply_watermark_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
        if file_path:
            self.image_path = file_path
            self.image = Image.open(file_path)
            self.image_label.configure(image=self.get_tk_image())
            self.save_button.configure(state=tk.NORMAL)

    def apply_watermark(self):
        watermark_text = self.watermark_text_entry.get()
        if not watermark_text:
            messagebox.showwarning("Warning", "Please enter watermark text.")
            return

        font = ImageFont.truetype("arial.ttf", 20)
        draw = ImageDraw.Draw(self.image)
        text_width, text_height = draw.textsize(watermark_text, font=font)
        x = self.image.width - text_width - 10
        y = self.image.height - text_height - 10
        draw.text((x, y), watermark_text, font=font, fill="black")  

        self.image_label.configure(image=self.get_tk_image())

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            self.image.save(file_path)
            messagebox.showinfo("Success", "Image saved successfully.")

    def get_tk_image(self):
        tk_image = self.image.resize((400, 400), Image.ANTIALIAS)
        return tk.PhotoImage(image=tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()