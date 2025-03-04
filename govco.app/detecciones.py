from ultralytics import YOLO
import os
import reporte

def detectar(ruta_img_analizar, dominio, ancho, alto):
    # Se carga el modelo entrenado
    directorio_script = os.path.dirname(__file__)
    ruta_modelo = os.path.join(directorio_script, 'modelo', "v30i.yolov11l.pt", "best.pt")
    modelo = YOLO(ruta_modelo)

    resultados = modelo.predict(ruta_img_analizar, save=True, conf=0.1, iou=0.1, augment=True, 
                                agnostic_nms=True, retina_masks=False, show_conf=True, line_width=2, 
                                save_txt=True, save_conf=True, save_crop=True, show=False, 
                                project='static', name=dominio, imgsz=(ancho, alto))
    
    detectados, no_detectados, ruta_img = reporte.get_reporte(resultados, dominio)
    return detectados, no_detectados, ruta_img
