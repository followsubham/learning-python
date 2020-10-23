# +++ Step 1: Evaluate several models +++
        from sklearn.ensemble import RandomForestRegressor
        # Define the models
        model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
        model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
        model_3 = RandomForestRegressor(n_estimators=100, criterion='mae', random_state=0)
        model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
        model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)
        models = [model_1, model_2, model_3, model_4, model_5]
        # To select the best model out of the five, we define a function `score_model()` below.
        # This function returns the mean absolute error (MAE) from the validation set.
        # Recall that the best model will obtain the lowest MAE.
        from sklearn.metrics import mean_absolute_error
        # Function for comparing different models
        def score_model(model, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
            model.fit(X_t, y_t)
            preds = model.predict(X_v)
            return mean_absolute_error(y_v, preds)
        for i in range(0, len(models)):
            mae = score_model(models[i])
            print("Model %d MAE: %d" % (i+1, mae))

# +++ Step 2: Generate test predictions +++
            # Fit the model to the training data
        my_model.fit(X, y)
        # Generate test predictions
        preds_test = my_model.predict(X_test)
        # Save predictions in format used for competition scoring
        output = pd.DataFrame({'Id': X_test.index,
                               'SalePrice': preds_test})
        output.to_csv('submission.csv', index=False)

# ========== Missing Values ==========

# +++ Step 1: Preliminary investigation +++
        # Shape of training data (num_rows, num_columns)
        print(X_train.shape)
        # Number of missing values in each column of training data
        missing_val_count_by_column = (X_train.isnull().sum())
        print(missing_val_count_by_column[missing_val_count_by_column > 0])

# +++ Step 2: Drop columns with missing values +++
        # Fill in the line below: get names of columns with missing values
        cols_with_missing = [col for col in X_train.columns
                             if X_train[col].isnull().any()]
        # Fill in the lines below: drop columns in training and validation data
        reduced_X_train =  X_train.drop(cols_with_missing, axis=1)
        reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)
        print("MAE (Drop columns with missing values):")
        print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

# +++ Step 3: Imputation +++
        from sklearn.impute import SimpleImputer
        # Imputation
        my_imputer = SimpleImputer()
        imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
        imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
        # Imputation removed column names; put them back
        imputed_X_train.columns = X_train.columns
        imputed_X_valid.columns = X_valid.columns
        print("MAE (Imputation):")
        print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))

# +++ Step 4: Generate test predictions +++
        # Imputation
        final_imputer = SimpleImputer(strategy='median')
        final_X_train = pd.DataFrame(final_imputer.fit_transform(X_train))
        final_X_valid = pd.DataFrame(final_imputer.transform(X_valid))
        # Imputation removed column names; put them back
        final_X_train.columns = X_train.columns
        final_X_valid.columns = X_valid.columns
        # Define and fit model
        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(final_X_train, y_train)
        # Get validation predictions and MAE
        preds_valid = model.predict(final_X_valid)
        print("MAE (Your approach):")
        print(mean_absolute_error(y_valid, preds_valid))
        # Preprocess test data
        final_X_test = pd.DataFrame(final_imputer.transform(X_test))
        # Get test predictions
        preds_test = model.predict(final_X_test)


# ========== Categorical Variables ==========

# +++Step 1: Drop columns with categorical data +++
        # Drop columns in training and validation data
        drop_X_train = X_train.select_dtypes(exclude=['object'])
        drop_X_valid = X_valid.select_dtypes(exclude=['object'])

# +++ Step 2: Label encoding +++
        # Columns that can be safely label encoded
        good_label_cols = [col for col in object_cols if
                           set(X_train[col]) == set(X_valid[col])]

        # Problematic columns that will be dropped from the dataset
        bad_label_cols = list(set(object_cols) - set(good_label_cols))
        print('Categorical columns that will be label encoded:', good_label_cols)
        print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)
        from sklearn.preprocessing import LabelEncoder
        # Drop categorical columns that will not be encoded
        label_X_train = X_train.drop(bad_label_cols, axis=1)
        label_X_valid = X_valid.drop(bad_label_cols, axis=1)
        # Apply label encoder
        label_encoder = LabelEncoder()
        for col in set(good_label_cols):
            label_X_train[col] = label_encoder.fit_transform(X_train[col])
            label_X_valid[col] = label_encoder.transform(X_valid[col])

# +++ Step 3: Investigating cardinality +++
        # Get number of unique entries in each column with categorical data
        object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
        d = dict(zip(object_cols, object_nunique))
        # Print number of unique entries by column, in ascending order
        sorted(d.items(), key=lambda x: x[1])
        # For large datasets with many rows, one-hot encoding can greatly expand the
        #size of the dataset. For this reason, we typically will only one-hot encode
        # columns with relatively low cardinality. Then, high cardinality columns can
        # either be dropped from the dataset, or we can use label encoding.
        # As an example, consider a dataset with 10,000 rows, and containing one
        # categorical column with 100 unique entries.
        # If this column is replaced with the corresponding one-hot encoding,
        # how many entries are added to the dataset?
        # If we instead replace the column with the label encoding,
        # how many entries are added?

# +++Step 4: One-hot encoding +++
        # Columns that will be one-hot encoded
        low_cardinality_cols = [col for col in object_cols if X_train[col].nunique() < 10]
        # Columns that will be dropped from the dataset
        high_cardinality_cols = list(set(object_cols)-set(low_cardinality_cols))
        print('Categorical columns that will be one-hot encoded:', low_cardinality_cols)
        print('\nCategorical columns that will be dropped from the dataset:', high_cardinality_cols)

        from sklearn.preprocessing import OneHotEncoder
        # Apply one-hot encoder to each column with categorical data
        OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
        OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[low_cardinality_cols]))
        OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[low_cardinality_cols]))
        # One-hot encoding removed index; put it back
        OH_cols_train.index = X_train.index
        OH_cols_valid.index = X_valid.index
        # Remove categorical columns (will replace with one-hot encoding)
        num_X_train = X_train.drop(object_cols, axis=1)
        num_X_valid = X_valid.drop(object_cols, axis=1)
        # Add one-hot encoded columns to numerical features
        OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
        OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)
