from tkinter import Tk, Menu, Canvas, filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self):
        self.root = Tk()
        self.root.title("图片查看器")
        self.root.resizable(False, False)
        self.image_path = None
        self.scale_factor = 1.0
        self.animation_steps = 10
        self.last_x = None
        self.last_y = None

        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<MouseWheel>", self.scale_image)
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag_image)
        self.canvas.bind("<ButtonRelease-1>", self.release_drag)

        self.create_menu()
        self.load_image()

        self.root.mainloop()

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="选择图片", command=self.browse_image)
        file_menu.add_command(label="退出", command=self.root.quit)

    def browse_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
        self.load_image()

    def load_image(self):
        if self.image_path:
            self.scale_factor = 1.0
            width, height = self.root.winfo_width(), self.root.winfo_height()

            image = Image.open(self.image_path)
            image.thumbnail((width, height))

            self.original_image = image.copy()  # 保存原始图像
            self.scaled_image = image
            self.scaled_photo = ImageTk.PhotoImage(self.scaled_image)
    
            self.original_width, self.original_height = self.original_image.size
            self.canvas.delete("all")
            self.canvas.create_image(width / 2, height / 2, image=self.scaled_photo)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def scale_image(self, event):
        direction = event.delta // 120
        self.scale_factor *= 1.1 if direction > 0 else 0.9
        self.animate_scale_effect()

    def animate_scale_effect(self):
        if self.scale_factor < 0.1:  # 限制最小缩放比例
            self.scale_factor = 0.1
        elif self.scale_factor > 10.0:  # 限制最大缩放比例
            self.scale_factor = 10.0

        image = self.original_image.copy()
        width, height = image.size
        new_width = int(width * self.scale_factor)
        new_height = int(height * self.scale_factor)

        image = image.resize((new_width, new_height))
        self.scaled_image = image
        self.animate_image()

    def animate_image(self):
        width, height = self.original_width, self.original_height
        resize_factor = self.scale_factor
        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)

        image = self.scaled_image.resize((new_width, new_height))
        self.scaled_photo = ImageTk.PhotoImage(image)

        self.canvas.delete("all")
        self.canvas.create_image(width / 2, height / 2, image=self.scaled_photo)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def start_drag(self, event):
        self.last_x = event.x
        self.last_y = event.y
        self.canvas.config(cursor="fleur")

    def drag_image(self, event):
        if self.last_x is not None and self.last_y is not None:
            delta_x = event.x - self.last_x
            delta_y = event.y - self.last_y

            self.canvas.move("all", delta_x, delta_y)

            self.last_x = event.x
            self.last_y = event.y

    def release_drag(self, event):
        self.last_x = None
        self.last_y = None
        self.canvas.config(cursor="")

ImageViewer()
