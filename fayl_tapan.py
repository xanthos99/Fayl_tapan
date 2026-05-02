import os

def get_size(file_path):
    """Faylın ölçüsünü hesablayır."""
    try:
        size_bytes = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
    except:
        return "N/A"

def smart_manager():
    # Axtarılan genişlənmələr
    formats = ('.pdf', '.docx', '.pptx', '.html', '.py', '.css', '.js', '.txt')
    root_path = '/storage/emulated/0/'
    
    found_files = []

    print("\n" + "╔" + "═"*78 + "╗")
    print(f"║{'FAYL SKANERİ VƏ İDARƏETMƏ PANELİ':^78}║")
    print("╚" + "═"*78 + "╝")
    
    print("🔍 Skan edilir, zəhmət olmasa gözləyin...\n")

    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith(formats):
                full_path = os.path.join(root, file)
                found_files.append(full_path)

    if not found_files:
        print("❌ Heç bir fayl tapılmadı.")
        return

    # Hər faylı öz çərçivəsində göstərmək
    for i, path in enumerate(found_files):
        size = get_size(path)
        filename = os.path.basename(path)
        
        print(f"┌{'─'*10}┬{'─'*67}┐")
        print(f"│ ID: {i:<5}│ FAYL: {filename[:60]:<60} │")
        print(f"├{'─'*10}┼{'─'*67}┤")
        print(f"│ YOL:     │ {path:<60} │")
        print(f"│ ÖLÇÜ:    │ {size:<60} │")
        print(f"└{'─'*10}┴{'─'*67}┘")

    print(f"\n📊 Toplam tapılan fayl: {len(found_files)}")
    print("="*80)
    
    print("\nSilmək istədiyiniz nömrəni (ID) yazın (məs: 0,3,7)")
    print("Çıxmaq üçün 'q' yazın.")
    
    choice = input("\n➤ SEÇİMİNİZ: ").strip()

    if choice.lower() == 'q':
        print("\n👋 Proqramdan çıxılır...")
        return

    try:
        indices = [int(x.strip()) for x in choice.split(',')]
        targets = [found_files[idx] for idx in indices if 0 <= idx < len(found_files)]
        
        if not targets:
            print("\n⚠️ Yanlış ID!")
            return

        print(f"\n🛑 XƏBƏRDARLIQ: {len(targets)} fayl silinəcək!")
        confirm = input("Təsdiq edirsiniz? (y/n): ").lower()

        if confirm == 'y':
            print("\n" + "─"*40)
            for target in targets:
                try:
                    os.remove(target)
                    print(f"🗑️  SİLİNDİ: {os.path.basename(target)}")
                except Exception as e:
                    print(f"❌ XƏTA: {os.path.basename(target)} -> {e}")
            print("─"*40)
        else:
            print("\n❌ Əməliyyat ləğv olundu.")
                
    except ValueError:
        print("\n❗ Səhv: Yalnız rəqəm daxil edin!")
    except Exception as e:
        print(f"\n❗ Gözlənilməz xəta: {e}")

if __name__ == "__main__":
    smart_manager()

