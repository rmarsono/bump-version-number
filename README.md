# Bump version number

Need to bump version number for React Native app releases

Current version is 1.0.31

in *package.json*
```
{"version": "1.0.31"}
```

Android version code is 85 - need to bump to 86; Android version name is 1.0.31 - need to bump to 1.0.32

in *android/build.gradle*
```
versionCode 85
versionName '1.0.31'
```

IOS marketing version is 1.0.31 - need to bump to 1.0.32; IOS current project version is 105 - need to bump to 106

in *ios/project/pbxproj*
```
CURRENT_PROJECT_VERSION = 105;
MARKETING_VERSION = 1.0.31;
```
