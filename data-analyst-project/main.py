import pandas as pd

# Membaca data CSV
def load_data(filename):
    return pd.read_csv(filename)

# Menampilkan daftar produk
def display_products(df):
    print("\nDaftar Produk:")
    print(df[['ProductID', 'ProductName', 'Category', 'Price', 'StockQuantity']])

# Memperbarui stok produk
def update_stock(df, product_id, new_stock):
    if product_id in df['ProductID'].values:
        df.loc[df['ProductID'] == product_id, 'StockQuantity'] = new_stock
        print(f"\nStok produk dengan ID {product_id} berhasil diperbarui.")
    else:
        print("\nProduk tidak ditemukan.")
    return df

# Menghitung total nilai inventaris
def calculate_inventory_value(df):
    df['InventoryValue'] = df['Price'] * df['StockQuantity']
    total_value = df['InventoryValue'].sum()
    print(f"\nTotal Nilai Inventaris: Rp {total_value:,.2f}")

def main():
    filename = 'inventory.csv'
    
    # Memuat data
    df = load_data(filename)
    
    # Menampilkan daftar produk
    display_products(df)
    
    # Memperbarui stok produk
    product_id = int(input("\nMasukkan ProductID untuk memperbarui stok: "))
    new_stock = int(input("Masukkan jumlah stok baru: "))
    df = update_stock(df, product_id, new_stock)
    
    # Menampilkan daftar produk setelah pembaruan
    display_products(df)
    
    # Menghitung dan menampilkan total nilai inventaris
    calculate_inventory_value(df)
    
    # Menyimpan perubahan ke file CSV
    df.to_csv(filename, index=False)
    
if __name__ == '__main__':
    main()
