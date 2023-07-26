import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tqdm import tqdm
import wizzair
import pandas as pd


from tkinter import ttk
from tqdm import tqdm
countries = {
    'ქუთაისი': 'KUT',
    'ერევანი': 'EVN',
    'Bahrain': 'BAH',
    'აკაბა ': 'AQJ',
    'ამანი': 'AMM',
    'ქუვეითი': 'KWI',
    'ბიშკეკი': 'FRU',
    'ლუქსემბურგი': 'LUX',
    'მალე (მალდივები)': 'MLE',
    'მასკატი': 'MCT',
    'სალალაჰი': 'SLL',
    'დამამი': 'DMM',
    'მედინა': 'MED',
    'რიადი': 'RUH',
    'ჯედა': 'JED',
    'სამარყანდი': 'SKD',
    'ტაშკენტი': 'TAS',
    'ვენა': 'VIE',
    'ზალცბურგი': 'SZG',
    'ბაქო': 'GYD',
    'კუკესი': 'KFZ',
    'ტირანა': 'TIA',
    'აბუ-დაბი': 'AUH',
    'დუბაი': 'DXB',
    'ბრიუსელი — შარლერუა': 'CRL',
    'ბანია-ლუკის აეროპორტი': 'BNX',
    'სარაევო': 'SJJ',
    'ტუზლა': 'TZL',
    'ბურგასი (შავი ზღვა)': 'BOJ',
    'ვარნა (შავი ზღვა)': 'VAR',
    'პლოვდივი': 'PDV',
    'სოფია ': 'SOF',
    'აბერდინი': 'ABZ',
    'ბირმინგემი': 'BHX',
    'ბრისტოლი': 'BRS',
    'ედინბურგი': 'EDI',
    'ლიდზი': 'LBA',
    'ლივერპული': 'LPL',
    'ლონდონი  (ნებისმიერი)': 'LON',
    'ლონდონი — ლუტონი': 'LTN',
    'ლონდონი-გატვიკი': 'LGW',
    'ბერლინ-ბრანდერბურგის': 'BER',
    'ბრემენი': 'BRE',
    'დორტმუნდი': 'DTM',
    'კარლსრუე/ბადენ-ბადენი': 'FKB',
    'კელნი': 'CGN',
    'მემინგენი/მიუნხენ-ვესტი': 'FMM',
    'ნიურნბერგი': 'NUE',
    'ფრანკფურტი — ჰანი': 'HHN',
    'ფრიდრიხსჰაფენი': 'FDH',
    'ჰამბურგის აეროპორტი': 'HAM',
    'ბილუნდი': 'BLL',
    'კოპენჰაგენი': 'CPH',
    'ორჰუსი': 'AAR',
    'Cairo (Sphinx)': 'SPX',
    'ალექსანდრია (ბორგ-ელ-არაბის)': 'HBE',
    'მარსა-ალამი': 'RMF',
    'სოჰაგი': 'HMB',
    'შარმ-ელ-შეიხი ': 'SSH',
    'ჰურგადა': 'HRG',
    'ალიკანტე': 'ALC',
    'ბარსელონა — ელ-პრატი': 'BCN',
    'ბილბაო': 'BIO',
    'ვალენსია ': 'VLC',
    'იბიცა': 'IBZ',
    'კასტელიონი (ვალენსია)': 'CDT',
    'მადრიდი': 'MAD',
    'მალაგა': 'AGP',
    'პალმა-დე-მალიორკა': 'PMI',
    'სანტანდერი': 'SDR',
    'სარაგოსა': 'ZAZ',
    'სევილია': 'SVQ',
    'ტენერიფე (კანარის კუნძულები)': 'TFS',
    'ფუერტევენტურა (კანარის კუნძულები)': 'FUE',
    'ტალინი': 'TLL',
    'ანკარა': 'ESB',
    'ანტალია': 'AYT',
    'დალამანი': 'DLM',
    'სტამბოლი': 'IST',
    'რეიკიავიკი': 'KEF',
    'ელიათი': 'ETM',
    'თელ-ავივი': 'TLV',
    'Comiso': 'CIY',
    'Lampedusa': 'LMP',
    'Milan Linate': 'LIN',
    'ალგერო (სარდინია)': 'AHO',
    'ანკონა': 'AOI',
    'ბარი': 'BRI',
    'ბოლონია': 'BLQ',
    'ბრინდიზი': 'BDS',
    'გენუა\r\nგენუა': 'GOA',
    'ვენეცია  (ნებისმიერი)': 'VEN',
    'ვენეცია — ტრევიზო': 'TSF',
    'ვენეციის მარკო პოლოს სახელობის აეროპორტი': 'VCE',
    'ვერონა': 'VRN',
    'კატანია (სიცილია)': 'CTA',
    'ლამეცია-ტერმე': 'SUF',
    'მილანი  (ნებისმიერი)': 'MIL',
    'მილანი — ბერგამო': 'BGY',
    'მილანი — მალპენსა ': 'MXP',
    'ნეაპოლი': 'NAP',
    'ოლბიის აეროპორტი': 'OLB',
    'პალერმო': 'PMO',
    'პერუჯა': 'PEG',
    'პესკარა': 'PSR',
    'პიზა (ტოსკანა)': 'PSA',
    'რიმინი': 'RMI',
    'რომი  (ნებისმიერი)': 'ROM',
    'რომი — ფიუმიჩინო': 'FCO',
    'რომი — ჩამპინო': 'CIA',
    'ტრიესტი': 'TRS',
    'ტურინი': 'TRN',
    'ლარნაკა': 'LCA',
    'პრიშტინა': 'PRN',
    'რიგა': 'RIX',
    'ვილნიუსი': 'VNO',
    'კაუნასი': 'KUN',
    'პალანგა — კლაიპედა ': 'PLQ',
    'მალტა': 'MLA',
    'Casablanca': 'CMN',
    'აგადირი': 'AGA',
    'მარაქეში': 'RAK',
    'პოდგორიცა': 'TGD',
    'ეინდჰოვენი': 'EIN',
    'ბერგენი': 'BGO',
    'ოლესუნი': 'AES',
    'ოსლო — სანეფიორ ტორპი': 'TRF',
    'ოსლო (ნებისმიერი)': 'OOS',
    'ოსლო გარდერმენი': 'OSL',
    'სტავანგერი': 'SVG',
    'ტრომსე': 'TOS',
    'ტრონჰეიმი': 'TRD',
    'ჰეუგესუნი': 'HAU',
    'ბიდგოშჩი': 'BZG',
    'გდანსკი': 'GDN',
    'ვარშავა — შოპენი': 'WAW',
    'ვროცლავი': 'WRO',
    'კატოვიცე': 'KTW',
    'კრაკოვი': 'KRK',
    'ლოძი': 'LCJ',
    'ლუბლინი': 'LUZ',
    'ოლშტინ-მაზურიის აეროპორტი': 'SZY',
    'პოზნანი': 'POZ',
    'ჟეშუვი': 'RZE',
    'შჩეცინი': 'SZZ',
    'ლისაბონი': 'LIS',
    'მადეირა': 'FNC',
    'პორტუ': 'OPO',
    'ფარუ': 'FAO',
    'Brasov': 'GHV',
    'ბაკეუ': 'BCM',
    'ბუქარესტი — ანრი კოანდა': 'OTP',
    'იასი': 'IAS',
    'კლუჟ-ნაპოკა': 'CLJ',
    'კონსტანცა': 'CND',
    'კრაიოვა': 'CRA',
    'სატუ-მარე': 'SUJ',
    'სიბიუ': 'SBZ',
    'სუჩავა': 'SCV',
    'ტიმიშოარა': 'TSR',
    'ტირგუ-მურეში': 'TGM',
    'კრასნოდარი ': 'KRR',
    'მოსკოვი — ვნუკოვო': 'VKO',
    'Kos': 'KGS',
    'ათენი': 'ATH',
    'ზაკინთოსი': 'ZTH',
    'კერკირა (კორფუ)': 'CFU',
    'კეფალონია': 'EFL',
    'მიკონოსი': 'JMK',
    'პრევეზა — აკტიონი': 'PVK',
    'როდოსი': 'RHO',
    'სალონიკი': 'SKG',
    'სანტორინი': 'JTR',
    'სკიათოსი': 'JSI',
    'ხანია (კრეტა)': 'CHQ',
    'ჰერაკლიონი\xa0(კრეტა)': 'HER',
    'ბაზელი-მიულუზი-ფრაიბურგი': 'BSL',
    'გრენობლი': 'GNB',
    'ლიონი': 'LYS',
    'ნიცა': 'NCE',
    'პარიზი — ბოვე': 'BVA',
    'პარიზი (ნებისმიერი)': 'PAR',
    'პარიზის ორლის': 'ORY',
    'ბელგრადი': 'BEG',
    'ნიში': 'INI',
    'ბრატისლავა': 'BTS',
    'კოშიცე': 'KSC',
    'პოპრად-ტატრი': 'TAT',
    'ლიუბლიანა': 'LJU',
    'ზაპოროჟიე': 'OZH',
    'კიევი — ჟულიანი': 'IEV',
    'კიევი (ნებისმიერი)': 'WKV',
    'ლვოვი': 'LWO',
    'ოდესა': 'ODS',
    'ხარკოვი': 'HRK',
    'ბორისპოლის საერთაშორისო აეროპორტი': 'KBP',
    'ბუდაპეშტი': 'BUD',
    'დებრეცენი': 'DEB',
    'ტურკუ': 'TKU',
    'ალმათის საერთაშორისო აეროპორტი': 'ALA',
    'ასტანა': 'NQZ',
    'გეტებორგი — ლანდვეტერი': 'GOT',
    'ვექშე': 'VXO',
    'მალმე': 'MMX',
    'სტოკჰოლმი — სკავსტა': 'NYO',
    'ჟენევა': 'GVA',
    'პარდუბიცე': 'PED',
    'პრაღა': 'PRG',
    'ოჰრიდი': 'OHD',
    'სკოპიე': 'SKP',
    'Dubrovnik': 'DBV',
    'სპლიტი': 'SPU'}


def message_to_window(message):
    message_label.config(text=message)
    message_label.update()
    text_widget.insert(tk.END, message + "\n")
    text_widget.see(tk.END)
    text_widget.update()


def worker(FROM, TO, INTERVAL, PRICE):

    FROM = FROM.upper()
    TO = TO.upper()
    INTERVAL = int(INTERVAL)
    USER_PRICE = int(PRICE)

    outboundflights = wizzair.get_dates_and_price(saidan=FROM, sad=TO, direct='outboundFlights')
    message_to_window("outbound flights loaded ")

    returnFlights = wizzair.get_dates_and_price(saidan=FROM, sad=TO, direct='returnFlights')
    message_to_window("return flights loaded ")

    df_lowest_price = pd.DataFrame(
        wizzair.get_Best_dates_for_rest(
            wizzair.find_best_price_range(outboundflights, 'dates'),
            wizzair.find_best_price_range(returnFlights, 'dates'),
            INTERVAL,
            price_for_gafrena=wizzair.find_best_price_range(outboundflights, 'price'),
            price_for_dabruneba=wizzair.find_best_price_range(returnFlights, 'price')
            )
    )

    # Define the Excel file name
    excel_file = 'dataLowerPrices.xlsx'

    # Save the DataFrame to an Excel file
    df_lowest_price.to_excel(excel_file, index=False)
    message_to_window(f"excel file {excel_file} generated succesfully ")


    just_prices = wizzair.get_only_uniq_prices_for_flights(outboundflights,returnFlights)
    message_to_window("uniq prices loaded ")

    if USER_PRICE in just_prices:
        df_user_price = pd.DataFrame(
            wizzair.get_Best_dates_for_rest(
                departure_dates=wizzair.user_requested_price_flights(
                    USER_PRICE, outboundflights),
                return_dates=wizzair.user_requested_price_flights(
                    USER_PRICE, returnFlights),
                interval=INTERVAL,
                price_for_gafrena=USER_PRICE,
                price_for_dabruneba=USER_PRICE
            )
        )

        excel_file2 = 'dataUserPrices.xlsx'
        df_user_price.to_excel(excel_file2, index=False)
        message_to_window(f"excel file {excel_file2} generated succesfully ")
    else:
        message_to_window("your prices is not in Wizzair prices")
        message_to_window(f'you can choose prices from list: {just_prices} ', )

    # Show a message box when done
    
    messagebox.showinfo("Task Complete", "proccess has finished!")


def submit():
    from_value = entry1.get()
    to_value = entry2.get()
    interval_value = entry3.get()
    user_price = entry4.get()

    if not all([from_value, to_value, interval_value, user_price]):
        messagebox.showerror("Error", "All fields are required!")
        return
    # Create a progress bar window
    progress_window = tk.Toplevel(window)
    progress_window.title("Loading...")

    progress_label = tk.Label(progress_window, text="Working...")
    progress_label.pack()

    # Create a label to display messages
    global message_label
    message_label = tk.Label(progress_window, text="")
    message_label.pack()

    progress_bar = ttk.Progressbar(
        progress_window, length=500, mode="indeterminate")
    progress_bar.pack()

    # Start the progress bar
    progress_bar.start()

    # Create a text widget to display messages
    global text_widget
    text_widget = tk.Text(progress_window, width=40, height=10)
    text_widget.pack()

    # Call worker() function in a separate thread
    def call_worker():
        worker(from_value, to_value, interval_value, user_price)

        # Stop the progress bar and close the progress bar window when done
        progress_bar.stop()
        progress_window.destroy()

    import threading
    threading.Thread(target=call_worker).start()


# Create the main window
window = tk.Tk()

# Set the window size
window.geometry("600x600")  # Width x Height

# Create labels for the input fields
label1 = tk.Label(window, text="FROM:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="TO:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

label3 = tk.Label(window, text="INTERVAL:")
label3.pack()

entry3 = tk.Entry(window)
entry3.pack()

label4 = tk.Label(window, text="USER_PRICE:")
label4.pack()

entry4 = tk.Entry(window)
entry4.pack()


# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()


# Start the main event loop
window.mainloop()
