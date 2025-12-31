
import Home from "./screens/Home/Home";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { NavigationContainer } from "@react-navigation/native";
import DetailCourse from "./screens/Home/DetailCourse";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import Discuss from "./screens/Discuss/Discuss"
import My from "./screens/User/My"
import { Icon, PaperProvider } from "react-native-paper";
import PageMaterials from "./screens/Material/PageMaterials";
import Study from "./screens/Discuss/Study";

const Stack = createNativeStackNavigator();
const StackNavigator = () => {
    return(
        <Stack.Navigator screenOptions={{headerShown: false}}>
            <Stack.Screen name="Course" component={Home} options={{title: "Khóa học"}}/>
            <Stack.Screen name="Course Detail" component={DetailCourse} options={{title: "Chi tiết khóa học"}}/>
        </Stack.Navigator>
    );
}

const Tab = createBottomTabNavigator();
const TabNavigator = () => {
     return(
        <Tab.Navigator screenOptions={{tabBarActiveTintColor: "blue" ,tabBarInactiveTintColor: "gray"}}>
            <Tab.Screen name="Home" component={StackNavigator} options={{title:"Home", tabBarIcon: ({color}) => <Icon source="home" size={25} color={color} />}}/>
            <Tab.Screen name="Marterials" component={PageMaterials} options={{title:"Tài liệu", tabBarIcon: ({color}) => <Icon source="file-document" size={25} color={color}/>}}/>
             <Tab.Screen name="Study" component={Study} options={{title:"Học tập", tabBarIcon: ({color}) => <Icon source="layers-edit" size={25} color={color}/>}}/>
            <Tab.Screen name="Discuss" component={Discuss} options={{title:"Thảo luận", headerShown: false, tabBarIcon: ({color}) => <Icon source="clouds" size={25} color={color}/>}}/>
            <Tab.Screen name="My" component={My} options={{title: "Tôi", tabBarIcon: ({color}) => <Icon source="account" size={25} color={color}/>}} />
        </Tab.Navigator>
     );
}

const App = () => {

    return(
       <PaperProvider>
         <NavigationContainer>
            <TabNavigator/>
        </NavigationContainer>
       </PaperProvider>
    );
}

export default App;