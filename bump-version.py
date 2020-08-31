# usage: python ./bump-version.py [IOS folder name] [version/Android versionName/IOS MARKETING_VERSION] [Android versionCode] [IOS CURRENT_PROJECT_VERSION]

# argument 1 = ios folder name
# argument 2 = version number/android versionName/IOS marketing version e.g. 1.0.30
# argument 3 = Android versionCode
# argument 4 = IOS CURRENT_PROJECT_VERSION

import sys

# file paths
packageJsonPath = 'package.json'
buildGradlePath = 'android/app/build.gradle'
projectXcodePath = 'ios/' + sys.argv[1] + '/project.pbxproj'

# package json
packageJson = open(packageJsonPath, 'r')
newPackageJson = ""

for line in packageJson:
  strippedLine = line.strip()
  if '"version":' in strippedLine:
    newLine = '"version": "' + sys.argv[2] + '",'
    newPackageJson += newLine + "\n"
  else:
    newPackageJson += strippedLine + "\n"
packageJson.close()

packageJson = open(packageJsonPath, 'w')
packageJson.write(newPackageJson)
packageJson.close()

print('*** updated version in package.json to ' + sys.argv[2])

# build.gradle
buildGradle = open(buildGradlePath, 'r')
newBuildGradle = ""

for line in buildGradle:
  strippedLine = line.strip()
  newLine = ""
  if "versionCode " in strippedLine:
    newLine = "versionCode " + sys.argv[3]
  elif "versionName " in strippedLine:
    newLine = 'versionName "' + sys.argv[2] + '"'
  else:
    newLine = strippedLine
  newBuildGradle += newLine + "\n"

buildGradle.close()

buildGradle = open(buildGradlePath, 'w')
buildGradle.write(newBuildGradle)
buildGradle.close()

print('*** updated Android versionCode to ' + sys.argv[3] + ' and versionName to ' + sys.argv[4])

# project.pbxproj
pbxProj = open(projectXcodePath, 'r')
newPbxProj = ""

for line in pbxProj:
  strippedLine = line.strip()
  newLine = ""
  if "CURRENT_PROJECT_VERSION " in strippedLine:
    newLine = "CURRENT_PROJECT_VERSION = " + sys.argv[4]
  elif "MARKETING_VERSION " in strippedLine:
    newLine = "MARKETING_VERSION " + sys.argv[2]
  else:
    newLine = strippedLine
  newPbxProj += newLine + "\n"

pbxProj.close()

pbxProj = open(projectXcodePath, 'w')
pbxProj.write(newPbxProj)
pbxProj.close()

print('*** updated IOS MARKETING_VERSION to ' + sys.argv[2] + ' and CURRENT_PROJECT_VERSION to ' + sys.argv[4])

print('*** successfully bumped version number')