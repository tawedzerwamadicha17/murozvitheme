from frappe import _

def get_bootinfo(bootinfo):  
    
    bootinfo.update({
        "murozvi_theme": {
            "version": "1.0.0",
            "brand_name": "Murozvi Enterprises", 
            "primary_color": "#1e3a8a",
            "secondary_color": "#dc2626",
            "font_family": "'Inter', sans-serif"
        }
    })
    
    return bootinfo  
