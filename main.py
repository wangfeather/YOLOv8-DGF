
#demopredict
# from ultralytics import YOLO
# yolo = YOLO("./yolov8n.pt",task="detect")
# result = yolo(source="/root/autodl-tmp/ultralytics/assets/aoteman.jpg",save=True)
#



from ultralytics import YOLO

if __name__ == '__main__':

    # 直接使用预训练模型创建模型.
    # 使用yaml配置文件来创建模型,并导入预训练权重,epoches=300.
    model = YOLO('/root/autodl-tmp/ultralytics/cfg/models/v8/underwater.yaml')    #网络结构的配置文件
    model.load('yolov8n.pt')            #传入模型的预训练权重
    model.train(**{'cfg': '/root/autodl-tmp/ultralytics/cfg/example.yaml',        #参数的配置文件
                   'data': '/root/autodl-tmp/datasets/underwater/data.yaml'})     #数据集的路径


    # # 模型验证
    # model = YOLO('/root/autodl-tmp/runs/detect/train/weights/best.pt')
    # model.val(**{'data': '/root/autodl-tmp/datasets/underwater/data.yaml'})


    # # 模型推理
    # model = YOLO('/root/autodl-tmp/runs/detect/train/weights/best.pt')
    # model.predict(source='/root/autodl-tmp/datasets/underwater/images/test', **{'save': True})

