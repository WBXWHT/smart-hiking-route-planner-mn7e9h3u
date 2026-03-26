import json
import random
import datetime
from typing import List, Dict, Any

class HikingRoutePlanner:
    """智能徒步路线规划助手核心类"""
    
    def __init__(self):
        """初始化模拟数据"""
        self.user_preferences = {
            "difficulty": "中等",
            "duration": "3-4小时", 
            "scenery": "山林湖泊",
            "elevation_gain": "300-500米"
        }
        
        self.geo_data = [
            {"id": 1, "name": "西山森林公园", "difficulty": "简单", "duration": "2小时", 
             "scenery": "森林观景", "elevation": 200, "popularity": 85},
            {"id": 2, "name": "香山红叶路线", "difficulty": "中等", "duration": "3小时",
             "scenery": "山林红叶", "elevation": 400, "popularity": 92},
            {"id": 3, "name": "灵山高山草甸", "difficulty": "困难", "duration": "5小时",
             "scenery": "高山草甸", "elevation": 800, "popularity": 78},
            {"id": 4, "name": "百望山环线", "difficulty": "中等", "duration": "3.5小时",
             "scenery": "山林湖泊", "elevation": 350, "popularity": 88},
            {"id": 5, "name": "凤凰岭古道", "difficulty": "中等", "duration": "4小时",
             "scenery": "古道奇石", "elevation": 450, "popularity": 82}
        ]
    
    def analyze_user_preferences(self) -> Dict[str, Any]:
        """分析用户偏好（模拟AI分析过程）"""
        print("正在分析用户运动偏好...")
        
        # 模拟AI分析逻辑
        analysis_result = {
            "preferred_difficulty": self.user_preferences["difficulty"],
            "preferred_duration": self.user_preferences["duration"],
            "preferred_scenery": self.user_preferences["scenery"],
            "analysis_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "confidence_score": round(random.uniform(0.7, 0.95), 2)
        }
        
        print(f"偏好分析完成，置信度: {analysis_result['confidence_score']}")
        return analysis_result
    
    def match_routes_with_ai(self, analysis_result: Dict[str, Any]) -> List[Dict[str, Any]]:
        """使用AI逻辑匹配推荐路线"""
        print("正在使用AI匹配个性化路线...")
        
        matched_routes = []
        for route in self.geo_data:
            # 模拟AI匹配算法
            score = 0
            
            # 难度匹配
            if route["difficulty"] == analysis_result["preferred_difficulty"]:
                score += 30
            elif abs(["简单", "中等", "困难"].index(route["difficulty"]) - 
                    ["简单", "中等", "困难"].index(analysis_result["preferred_difficulty"])) == 1:
                score += 15
            
            # 风景类型匹配
            if analysis_result["preferred_scenery"] in route["scenery"]:
                score += 25
            
            # 考虑路线热度
            score += route["popularity"] * 0.2
            
            # 模拟大模型生成推荐理由
            if score > 60:
                reasons = [
                    f"符合您偏爱的{analysis_result['preferred_scenery']}风景",
                    f"难度{route['difficulty']}适合您的体能水平",
                    f"全程约{route['duration']}，时间安排合理"
                ]
                
                matched_route = route.copy()
                matched_route["match_score"] = min(score, 100)
                matched_route["recommendation_reason"] = random.choice(reasons)
                matched_route["ai_generated"] = True
                matched_routes.append(matched_route)
        
        # 按匹配分数排序
        matched_routes.sort(key=lambda x: x["match_score"], reverse=True)
        return matched_routes[:3]  # 返回前3个推荐
    
    def generate_personalized_plan(self) -> Dict[str, Any]:
        """生成个性化路线规划"""
        print("=" * 50)
        print("智能徒步路线规划助手")
        print("=" * 50)
        
        # 步骤1: 分析用户偏好
        analysis = self.analyze_user_preferences()
        
        # 步骤2: AI匹配路线
        recommendations = self.match_routes_with_ai(analysis)
        
        # 步骤3: 生成最终规划
        plan = {
            "user_id": "user_001",
            "generation_time": datetime.datetime.now().isoformat(),
            "preference_analysis": analysis,
            "recommended_routes": recommendations,
            "plan_summary": f"为您找到{len(recommendations)}条匹配路线",
            "success_rate": "25%"  # 模拟项目成果数据
        }
        
        return plan
    
    def display_plan(self, plan: Dict[str, Any]):
        """展示路线规划结果"""
        print("\n" + "=" * 50)
        print("个性化路线规划结果")
        print("=" * 50)
        
        print(f"生成时间: {plan['generation_time']}")
        print(f"分析置信度: {plan['preference_analysis']['confidence_score']}")
        print(f"核心功能采纳率提升: {plan['success_rate']}")
        
        print("\n推荐路线:")
        for i, route in enumerate(plan['recommended_routes'], 1):
            print(f"\n{i}. {route['name']}")
            print(f"   匹配度: {route['match_score']:.1f}分")
            print(f"   难度: {route['difficulty']} | 时长: {route['duration']}")
            print(f"   海拔爬升: {route['elevation']}米")
            print(f"   推荐理由: {route['recommendation_reason']}")
            print(f"   AI生成: {'是' if route.get('ai_generated') else '否'}")

def main():
    """主函数 - 程序入口"""
    try:
        # 创建路线规划器实例
        planner = HikingRoutePlanner()
        
        # 生成个性化规划
        plan = planner.generate_personalized_plan()
        
        # 展示结果
        planner.display_plan(plan)
        
        # 保存结果到JSON文件（模拟数据持久化）
        with open("hiking_plan.json", "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)
        
        print("\n" + "=" * 50)
        print("规划已保存至 hiking_plan.json")
        print("=" * 50)
        
    except Exception as e:
        print(f"程序执行出错: {e}")

if __name__ == "__main__":
    main()