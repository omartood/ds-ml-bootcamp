### **Explaining My decisions for each step**

### **Step 1: Load & Inspect**

* **What was done:**     Waxaa Soo load-garesanay dataset keena, kadib waxan Fiirinay ama hubinay waxa aan hesano iyo siday uyalan anaga oo isticmalayna qaar kammidaa Methodeths-ka inspect lagu sameyo ee Pandas leedaha Sida  `.head()`, `.isnull().sum()`, and `.shape` methods.

### **Step 2: Clean Target Formatting (Price)**

* **What was done:** Target-keena ayaa Kanadafinay Symbols-ka iyo **,** and then waxan ubadalnay Float type ama Tiropointaqbasha madaama Lacagta Marmarka qaar ceint laisticmalo.

### **Step 3: Fix Category Errors before Imputation**

* **What was done:** madaama uu Location Col uu yahay String kaas oo u habeesan Category Compuer-kana UU fahmo 0 ans 1's waxan sameeye inaa Ka filter kareyo samples-ka aan eheen wax waxmicnaa sameenayo sida kuwa leh "??" iyo "Type Error"" ayaa waxa ubadalnay wax micno samenayo iyo Nan value kas noo  ogolanayo inaa uuxino mise aan Sifudud ku Access-gareno.

### **Step 4: Impute Missing Values**

* **What was done:** Missing values waxa yeeshay kaliyaa Sedex  columns:
* Odometer_km    **7**
* Doors          **7**
* Location       **5**
  Madaama Dataset-keena uu yaraa waxan door biday ina buuxino inta remove gareenlahaay.
* * `Odometer_km`: Waxan kubuuxinay Avg **Median** aniga oo kafoganayo in mean ii keeno qiimo kayara badan  kan mediam , mode asna waxa uga tagay madaama lagayabo in uu isiiyo Skew tiro dataset dhinac u badan .
  * `Doors`: Waxan u isticmalay **mode** (most frequent value) madaama qiimaha zaid ukala badneen.
  * `Location`: waxa u isticmalay  **mode** madaama uuu aha "String" category kas oo mean, iyo  median aqbalayn.

### **Step 5: Remove Duplicates**

* **What was done:** Waxan remove garenay dhaman Duplicates-kii ku jiray data anaga oo u isticmalnay  `.drop_duplicates()` method. waxana Arki karta shap-ka data-dayna ka hor iyo ka dib

### **Step 6: Outliers (IQR capping)**

* **What was done:**  Outliers in `Price` and `Odometer_km` columns  ayaa ka saaray anigoo adeegsanayo IQR method kaas oo aan u samey Func kaas oo noo xisabinayo lower, upper bounds-keena kadhibna Clip() ayaan ku sameeye si aan Outliers ka aan ugu badalo.

### **Step 7: One-Hot Encode Categorical(s)**

* **What was done:**  `Location` column madaama uu aha "string"" u habesan category waxan u badalnay Binary cols  anaga u marnay  `pd.get_dummies()`. kkas  oo kala jabilayo category kasta una samenayo col cusub.

### **Step 8: Feature Engineering**

* **What was done:** Three new features were created from the existing data:
  * `Car_Age`: waa inta sano uu jiro
  * `News_with_No_Accident`: column-kan waxa ku ogaaneyna gariga in uu cusub yahay iyo  inkle anago ku soo bandhigeeno as binary.
  * `Super_Car`: Gaariga inoogu fican ee iinoyaal xaga da'da iyo shilla'aanta  `News_with_No_Accident` feature iyo  `Doors`.
  * `Best_Seller`: A binary feature based on `Car_Age` and `Odometer_km`.
  * `Log_Price`: Target-kiina oo an ku sameenay log transformation  `Price` column.

### **Step 9: Feature Scaling**

* **What was done:** The numerical features intended for the model's input were scaled using `StandardScaler`. The `Price`, `Log_Price`, and the new binary engineered features were explicitly excluded from this scaling process.

### **Step 10: Final Checks & Save**

* **What was done:** final dataset-kena oo an inspect-gareno ama xaqiijiyo inoo no saxanyahay sida missing v and shape. The cleaned dataset was then saved.
