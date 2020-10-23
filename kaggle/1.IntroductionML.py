# ========== Explore Your Data ==========

# +++ Step 1: Loading Data +++
        import pandas as pd
        # Path of the file to read
        iowa_file_path = '../input/home-data-for-ml-course/train.csv'
        # Fill in the line below to read the file into a variable home_data
        home_data = pd.read_csv(iowa_file_path)

# ========== First Machine Learning Model ==========

# +++ Step 1: Create the list of features below +++
        feature_names = ["LotArea","YearBuilt","1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr","TotRmsAbvGrd"]
        # Select data corresponding to features in feature_names
        X = home_data[feature_names]

# +++ Step 2: specify the model +++
        from sklearn.tree import DecisionTreeRegressor
        #specify the model. For model reproducibility, set a numeric value for random_state
        # when specifying the model
        iowa_model = DecisionTreeRegressor(random_state=1)
# +++ Step 3: Fit the model +++
        iowa_model.fit(X, y)

# +++ Step 4 Make Predictions +++
        predictions = iowa_model.predict(X)
        print(predictions)

# ========== Model Validation ==========

# +++ Step 1: Split Your Data +++
        from sklearn.model_selection import train_test_split

# +++ Step 2: Specify and Fit the Model +++
        train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=1)
        # You imported DecisionTreeRegressor in your last exercise and that code has been copied
        # to the setup code above. So, no need to import it again Specify the model
        iowa_model = DecisionTreeRegressor(random_state=1)
        # Fit iowa_model with the training data.
        iowa_model.fit(train_X, train_y)
# +++ Step 3: Make Predictions with Validation data +++
        val_predictions = iowa_model.predict(val_X)
# +++ Step 4: Calculate the Mean Absolute Error in Validation Data +++
        from sklearn.metrics import mean_absolute_error
        val_mae = mean_absolute_error(val_predictions, val_y)

# ========== Underfitting and Overfitting ==========

# +++ Step 1: Compare Different Tree Sizes +++
        candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
        # Write loop to find the ideal tree size from candidate_max_leaf_nodes
        scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
        # Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
        best_tree_size = min(scores, key=scores.get)
# +++ Step 2: Fit Model Using All Data +++
        # Fill in argument to make optimal size and uncomment
        final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)
        # fit the final model and uncomment the next two lines
        final_model.fit(X, y)

# ========== Random Forests ==========

# +++ Step 1: Use a Random Forest +++
        from sklearn.ensemble import RandomForestRegressor
        # Define the model. Set random_state to 1
        rf_model = RandomForestRegressor()
        # fit your model
        rf_model.fit(train_X, train_y)
        # Calculate the mean absolute error of your Random Forest model on the validation data
        rf_val_predictions = rf_model.predict(val_X)
        rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)
        print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))

# ========== Automated machine learning (AutoML) ==========

# TODO: Fill in your project ID and bucket name
        PROJECT_ID = 'your-project-id-here'
        BUCKET_NAME = 'your-bucket-name-here'

        # Do not change: Fill in the remaining variables
        DATASET_DISPLAY_NAME = 'house_prices_dataset'
        TRAIN_FILEPATH = "../input/house-prices-advanced-regression-techniques/train.csv"
        TEST_FILEPATH = "../input/house-prices-advanced-regression-techniques/test.csv"
        TARGET_COLUMN = 'SalePrice'
        ID_COLUMN = 'Id'
        MODEL_DISPLAY_NAME = 'house_prices_model'
        TRAIN_BUDGET = 2000

        # Do not change: Create an instance of the wrapper
        from automl_tables_wrapper import AutoMLTablesWrapper

        amw = AutoMLTablesWrapper(project_id=PROJECT_ID,
                                  bucket_name=BUCKET_NAME,
                                  dataset_display_name=DATASET_DISPLAY_NAME,
                                  train_filepath=TRAIN_FILEPATH,
                                  test_filepath=TEST_FILEPATH,
                                  target_column=TARGET_COLUMN,
                                  id_column=ID_COLUMN,
                                  model_display_name=MODEL_DISPLAY_NAME,
                                  train_budget=TRAIN_BUDGET)
# Do not change: Create and train the model
amw.train_model()

# Do not change: Get predictions
amw.get_predictions()